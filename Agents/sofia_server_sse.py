from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SofiaServer")

import geopy.distance
import pandas as pd
import requests
import variables as vars
from sqlalchemy import desc
import time

from framework.orm import UserCreated, SessionLocal, AddressSearch

import googlemaps

local_data = {
    
}




def save_coverage(
        user_id, 
        user_address,  
        lat, 
        lon, 
        llm_address, 
        llm_coverage_status
        ):
    """""

    Function to save the coverage search to the database

    Args:
    - user_id: string with the id of the user
    - user_address: string with the address of the user
    - lat: float with the latitude
    - lon: float with the longitude
    - llm_address: string with the address of the coverage point
    - llm_coverage_status: string with the coverage status


    """
    with SessionLocal() as session:
        new_search = AddressSearch(
            user_id=user_id,
            user_address=user_address,
            llm_address=llm_address,
            llm_latitude=lat,
            llm_longitude=lon,
            llm_coverage_status=llm_coverage_status,
        )
        session.add(new_search)
        session.commit()

def check_coverage(lat, lon, id_user):
    """
    Function to check if latitud and longitud are covered by the service and if it is critical user

    Args:
    - lat: float with the latitude
    - lon: float with the longitude
    - id_user: string with the id of the user

    Returns:
    - dict with the result of the validation

    Example output:
    {
        "cobertura": "SI",
        "error": "NO"
        "is_critical": True
    }
    """
    # calculate distances
    print(local_data["last_update"])
    distances: pd.DataFrame = local_data["coverage"].apply(lambda x: geopy.distance.distance((lat, lon), (x["LATITUD"], x["LONGITUD"])).m, axis=1)
    # check if the point is covered
    with SessionLocal() as session:
        address_search = session.query(AddressSearch).filter(AddressSearch.user_id == id_user).order_by(desc(AddressSearch.updated_at)).first()
        if distances.min() <= vars.GEO_MAX_DISTANCE:
            idxmin = distances.idxmin()
            address_search.llm_coverage_status = True
            result = {"cobertura": "SI", "error": "NO", "is_critical": local_data["coverage"].loc[idxmin]["IS_CRITICAL"]}
  
        else:
            address_search.llm_coverage_status = False
            result = {"cobertura": "NO", "error": "NO", "is_critical": False}
        session.commit()
        return result
    
def lat_lon_check_address(lat, lon, id_user):
    """
    Function to get the address from a latitude and longitude"

    Args:
    - lat: float with the latitude
    - lon: float with the longitude
    - id_user: string with the id of the user

    Returns:
    - dict with the result of the validation

    Example output:
    {
        "address": "Venezuela 3155, Vicente Lopez, Buenos Aires, Argentina",
        "error": "NO"
    }
    """
    params = {
        'latlng': f"{lat},{lon}",
        'key': vars.GOOGLE_API_KEY
    }
    resp = requests.get(url=vars.API_GOOGLE, params=params)
    if resp.status_code != 200:
        return {"error": "API request failed", "address": ""}
    else:
        data = resp.json()
        
        if len(data["results"]) == 0:
            return {"error": "No results found", "address": ""}
        else:
            addres = data["results"][0]["formatted_address"]
            save_coverage(
                id_user,
                addres,
                lat,
                lon,
                None,
                False,
            )
            return {"error": "NO", "address": addres}

def address_check_coverage(address, county, state, country, id_user):
    """ 
    Function to validate is an address is covered by the service and if it is critical user
    
    Args:
    - address: string with the address to check
    - county: string with the county/city of the address    
    - state: string with the state/province/department of the address
    - id_user: string with the id of the user
    
    Returns:
    - dict with the result of the validation
    
    Example output:
    {
        "cobertura": "SI",
        "error": "NO"
        "is_critical": True
    }
    """
    # process address"
    # api request
    gmaps = googlemaps.Client(key=vars.GOOGLE_API_KEY)

    full_address = address + ", " + county + ", " + state + ", " + country
    # Geocoding an address
    geocode_result = gmaps.geocode(full_address)
    if len(geocode_result) > 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        save_coverage(
                id_user,
                full_address,
                lat,
                lon,
                None,
                None,
            )
        return check_coverage(lat, lon, id_user)
    

    params = dict(
        text=full_address,
        apiKey=vars.GEO_API_KEY,
    )
    resp = requests.get(url=vars.GEO_API_URL, params=params)
    if resp.status_code != 200:
        return {"cobertura": "NO", "error": "API request failed"}
    else:
        data = resp.json()
        if len(data["features"]) == 0:
            return {"cobertura": "NO", "error": "No results found"}
        else:
            
            lat = data["features"][0]["properties"]["lat"]
            lon = data["features"][0]["properties"]["lon"]
            save_coverage(
                id_user,
                full_address,
                lat,
                lon,
                None,
                None,
            )
            return check_coverage(lat, lon, id_user)


def get_internet_plans(is_client, is_critical):
    """
        Function to get the internet plans for a client and criticality. Use only when the user has said whether is a client or not.

        Args:
        - is_client: boolean indicating if the user is a client
        - is_critical: boolean indicating if the user is critical

        Returns:
        - list of dictionaries with the plans and prices
        
        Example output:
        [
            {
                "Plan": "Movistar Fibra 300Mb",
                "Precio": 18000
            },
            {
                "Plan": "Movistar Fibra 1 Gb",
                "Precio": 27240
            }
        ]
    """
    client_prefix = "" if is_client else "not_"
    critical_prefix = "" if is_critical else "not_"
    client_type = client_prefix + "client_" + critical_prefix + "critical"
    selected_planes = local_data["plans"][["Plan", client_type]].dropna()
    selected_planes.rename(columns={client_type: "Precio"}, inplace=True)
    return selected_planes[["Plan", "Precio"]].to_dict(orient="records")


def save_to_db(id_user, plan, titular, dni, direccion, telefono, correo, cliente, precio):
    """
    Function to save the user data to the database when the user has confirmed all information is OK.
    
    Args:
    - id_user: string with the id of the user
    - plan: string with the plan selected
    - titular: string with the name of the titular
    - dni: string with the dni of the titular
    - direccion: string with the address of the user
    - telefono: string with the phone number of the user
    - correo: string with the email of the user
    - cliente: boolean indicating if the user is a client
    - precio: int with the price of the plan

    Returns:
    - dict with the user data saved

    """
    print("Saving to db")
    with SessionLocal() as session:
        new_user = UserCreated(
            plan=plan,
            titular=titular,
            dni=dni,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            cliente=cliente,
            precio=precio,
            credit_card="0000000000000000",
            user_id=id_user
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return new_user


# Transport stdio tells the server to:
# - Use standard input/output for communication.
# - Listen for requests on stdin and send function call responses to stdout.


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
