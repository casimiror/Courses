from mcp.server.fastmcp import FastMCP


import geopy.distance
import pandas as pd
import requests
import variables as vars
from sqlalchemy import desc
import time

from tools.sofia.tables.table import UserCreated, SessionLocal, AddressSearch

import googlemaps

local_data = {
    
}


def tool_init(mcp: FastMCP):
    """
    Function to initialize the tools. It loads the data from the local files and stores it in the local_data dictionary.
    """
    local_data["coverage"] = pd.read_csv("coverage.csv")
    local_data["last_update"] = time.time()
    local_data["plans"] = pd.read_csv("plans.csv")

    @mcp.tool(name="check_coverage", description="Check if the latitude and longitude are covered by the service")
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
        
        if distances.min() <= vars.GEO_MAX_DISTANCE:
            idxmin = distances.idxmin()
            result = {"cobertura": "SI", "error": "NO", "is_critical": local_data["coverage"].loc[idxmin]["IS_CRITICAL"]}
        else:
            result = {"cobertura": "NO", "error": "NO", "is_critical": False}
            return result
    
    @mcp.tool(name="lat_lon_check_address", description="Get the address from a latitude and longitude")
    def lat_lon_check_address(lat, lon, id_user):
        """
        Function to get the address from a latitude and longitude

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
                return {"error": "NO", "address": addres}
            

    @mcp.tool(name="address_check_coverage", description="Check if an address is covered by the service")
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
                return check_coverage(lat, lon, id_user)

    @mcp.tool(name="get_internet_plans", description="Get the internet plans for a client and criticality")
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

