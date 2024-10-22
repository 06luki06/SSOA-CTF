from sqlalchemy import create_engine, text

from environment import DATABASE_URL, PG_SCHEMA

# Create an engine
engine = create_engine(DATABASE_URL)


def create_nuclear_schema():
    # Connect to the database
    with engine.connect() as connection:
        # Begin a transaction
        with connection.begin():
            # Execute the SQL command to create the schema if it doesn't exist
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {PG_SCHEMA}"))


if __name__ == "__main__":
    create_nuclear_schema()
    print("Schema has been created (if it did not already exist).")
