from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User
from config import HOMER_USERNAME, HOMER_PASSWORD, BURNS_USERNAME, BURNS_PASSWORD
from passlib.hash import bcrypt
import random
import string

# Create the database tables
Base.metadata.create_all(bind=engine)

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def seed_users():
    session = SessionLocal()

    # Hash passwords
    homer_hashed_password = bcrypt.hash(HOMER_PASSWORD)
    burns_hashed_password = bcrypt.hash(BURNS_PASSWORD)

    # Define names
    names = [
        "Waylon Smithers",
        "Carl Carlson",
        "Lenny Leonard",
        "Frank Grimes",
        "Mindy Simmons",
        "Sherri Mackleberry",
        "Terri Mackleberry",
        "Hank Scorpio",
        "Don Delgrosso",
        "Eugene Fisk",
        "Howard K. Duff VIII",
        "Jack Marley",
        "Fred Kranepool",
        "Llewellyn Sinclair",
        "Charlie Montelongo",
        "Melvin Powell",
        "Dave Shutton"
    ]

    users = []

    # Create Homer Simpson
    homer = User(
        username=HOMER_USERNAME,
        name="Homer Simpson",
        password=homer_hashed_password,
        is_admin=False
    )
    users.append(homer)

    # Generate other employees
    for name in names:
        firstname, *lastnames = name.split()
        lastname = ''.join(lastnames)
        username = firstname[0].lower() + lastname[0].upper() + lastname[1:].lower()
        password = bcrypt.hash(random_password())
        user = User(
            username=username,
            name=name,
            password=password,
            is_admin=False
        )
        users.append(user)

    # Insert Mr. Burns
    burns = User(
        username=BURNS_USERNAME,
        name="Charles Montgomery Burns",
        password=burns_hashed_password,
        is_admin=True
    )
    users.append(burns)

    # Add users to session and commit
    session.add_all(users)
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_users()
