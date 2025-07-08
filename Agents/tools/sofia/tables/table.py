from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import Text

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import variables as vars

def connect_db():
    #_load_db_vars()
    # create db create_engine
    db = create_engine(vars.PG_CONN_STR + '/' + vars.DBNAME)
    return db


Base = declarative_base()

class UserCreated(Base):
    __tablename__ = 'user_created'

    id = Column(Integer, autoincrement=True, primary_key=True)
    plan = Column(String)
    titular = Column(String)
    dni = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    correo = Column(String)
    cliente = Column(String)
    precio = Column(String)
    credit_card = Column(String)
    user_id = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class UserConversation(Base):
    __tablename__ = 'user_conversation'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    conversation = Column(JSONB)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    enable_user = Column(Boolean, default=True)
    total_tokens = Column(Integer, default=0)

    def get_basic_info(self):
        return {
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Coverage(Base):
    __tablename__ = 'coverage'

    id = Column(Integer, autoincrement=True, primary_key=True)
    PRODUCTO= Column(String)
    FECHA_IMPORTAC= Column(String)
    FECHA_VIGENCIA= Column(String)
    CENTRAL= Column(String)
    MANZANA= Column(String)
    LATITUD= Column(Float)
    LONGITUD= Column(Float)
    PARES_LIBRES= Column(String)
    TX_CENTRAL= Column(String)
    LOCALIDAD= Column(String)
    CENTRAL_ORIGEN= Column(String)
    CENTRAL_CRITICA= Column(String)
    IS_CRITICAL= Column(Boolean)    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class ServicePlans(Base):
    __tablename__ = 'service_plans'

    id = Column(Integer, autoincrement=True, primary_key=True)
    Plan = Column(String)
    client_critical = Column(Integer)
    not_client_critical = Column(Integer)
    client_not_critical = Column(Integer)
    not_client_not_critical = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class LLMToolsInputs(Base):
    __tablename__ = 'llm_tools_inputs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    function_info = Column(JSONB)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class AddressSearch(Base):
    __tablename__ = 'fail_address_search'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    user_address = Column(String)
    user_locality = Column(String)
    user_state = Column(String)
    llm_address = Column(String)
    llm_locality = Column(String)
    llm_state = Column(String)
    llm_latitude = Column(Float)
    llm_longitude = Column(Float)
    llm_coverage_status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class UserObservations(Base):
    __tablename__ = 'user_observations'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    observations = Column(JSONB)
    is_complex_situation = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class IntegrationService(Base):
    __tablename__ = 'integration_service'

    id = Column(Integer, autoincrement=True, primary_key=True)
    integration_service_name = Column(String)
    integration_service_type = Column(String)
    integration_service_status = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class MessageStatus(Base):
    __tablename__ = 'service_status'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    service_name = Column(String)
    integration_service_id = Column(Integer)
    message_status = Column(Text)
    message_type = Column(String)
    channel_type = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

engine = connect_db()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)