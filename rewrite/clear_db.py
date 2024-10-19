from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Reusable engine, session, and base class setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def init_db():
    try:
        # Create a session
        session = SessionLocal()

        # Drop the tables using CASCADE
        session.execute(text("DROP TABLE IF EXISTS nuclear.comments CASCADE;"))
        session.execute(text("DROP TABLE IF EXISTS nuclear.employees CASCADE;"))

        # Commit the transaction (even though DROP doesn't require a commit in Postgres, it's good practice)
        session.commit()

        print("Database cleared successfully")
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    init_db()
