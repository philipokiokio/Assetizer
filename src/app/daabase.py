from sqlalchemy import create_engine

# sqlalchemy imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# application import
from src.app.config import db_settings

# Database URL instialized
DB_URL = f"postgresql://{db_settings.username}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}"

# Creating DB Session and Session Control
db_engine = create_engine(DB_URL)


Session_Factory = sessionmaker(autoflush=False, autocommit=False, bind=db_engine)


SessionLocal = scoped_session(Session_Factory)

# used for creating table
Base = declarative_base()
