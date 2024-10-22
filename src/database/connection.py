from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from environment import PG_SCHEMA, DATABASE_URL

# Create engine with connect_args to use the nuclear schema
engine = create_engine(
    DATABASE_URL,
    connect_args={'options': f"-csearch_path={PG_SCHEMA}"}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base declarative class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()