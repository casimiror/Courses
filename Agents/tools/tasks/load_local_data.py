from tools.sofia.tools import local_data

import pandas as pd
import variables as vars
import time

from gen_deps.logger import create_logger

from tools.sofia.tables.table import engine, Coverage, ServicePlans


_logger = create_logger("response_synthesizer:tasks")

def load_data():
    """
    Function to load the data from the database and the local data

    """
    last_update = local_data.get("last_update", 0)
    if time.time() - local_data.get("last_update", 0) < 86400:
        return
    
    _logger.info(f"Loading data {last_update}")
    PUNTOS = pd.read_sql_table(str(Coverage.__tablename__), engine)
    PUNTOS = PUNTOS.astype(
        {
            "PARES_LIBRES": int
        }
    )
    local_data["last_update"] = time.time()
    local_data["coverage"] = PUNTOS.loc[PUNTOS["PARES_LIBRES"] > 0]
    local_data["plans"] = pd.read_parquet(vars.PLANES_PATH)
    _logger.info(f"Data loaded {local_data.keys()}")


def load_coverage_plans_tables():
    """
    Function to load coverage and plans tables from parquet files
    """
    PUNTOS = pd.read_parquet(vars.COVERAGE_PATH)
    PLANES = pd.read_parquet(vars.PLANES_PATH)
    PLANES = PLANES.fillna(0)
