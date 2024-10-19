from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Create engine with connect_args to use the nuclear schema
engine = create_engine(
    DATABASE_URL,
    connect_args={'options': '-csearch_path=nuclear'}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base declarative class for models
Base = declarative_base()