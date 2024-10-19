from sqlalchemy import create_engine, text
from config import DATABASE_URL

# Create an engine
engine = create_engine(DATABASE_URL)

def create_nuclear_schema():
    # Connect to the database
    with engine.connect() as connection:
        # Begin a transaction
        with connection.begin():
            # Execute the SQL command to create the schema if it doesn't exist
            connection.execute(text('CREATE SCHEMA IF NOT EXISTS nuclear'))

if __name__ == "__main__":
    create_nuclear_schema()
    print("Schema 'nuclear' has been created (if it did not already exist).")
