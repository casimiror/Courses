import os
from pathlib import Path

from sqlalchemy import make_url

CUR_DIR = Path(os.path.dirname(os.path.realpath(__file__)))


DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
NO_OF_WORKERS = os.getenv("NO_OF_WORKERS", 2 if DEBUG else 4)

DBNAME = os.getenv("DBNAME", "vectordb")
PG_CONN_STR = os.getenv("PG_CONNECTION_URL", "postgresql://testuser:testpwd@pgvector:5432")
APG_CONN_STR = ""
PG_URL = make_url(PG_CONN_STR)
PG_CONNECTION_DICT = {
    'dbname': DBNAME,
    'user': PG_URL.username,
    'password': PG_URL.password,
    'host': PG_URL.host,
}

GEO_API_URL = 'https://api.geoapify.com/v1/geocode/search'
GEO_MAX_DISTANCE = 150
COVERAGE_PATH = "temp/Artori/cobertura.parquet"
PLANES_PATH = "temp/Artori/planes.parquet"
GEO_API_KEY = os.getenv("GEO_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
API_GOOGLE = "https://maps.googleapis.com/maps/api/geocode/json"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "") 
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
BEARER_TOKEN = "bearer " + os.getenv("BEARER_TOKEN", "")