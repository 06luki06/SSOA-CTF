from database import SessionLocal, Base
from models import User
from validate import UserCreate
from config import HOMER_PASSWORD, BURNS_PASSWORD
import hashlib
import random
import string

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def md5_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def generate_username(firstname: str, lastname: str) -> str:
    return firstname[0].lower() + lastname.capitalize()

def seed_users():
    # Create a new session
    session = SessionLocal()
    try:
        # Create the database tables in the 'nuclear' schema
        Base.metadata.create_all(bind=session.bind)

        # Define names
        names = [
            "Waylon Smithers",
            "Carl Carlson",
            "Lenny Leonard",
            "Frank Grimes",
            "Homer Simpson",
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
            "Charles Montgomery Burns",
            "Melvin Powell",
            "Dave Shutton"
        ]

        users = []

        # Generate users
        for name in names:
            firstname, *lastnames = name.split()
            lastname = ''.join(lastnames)
            username = generate_username(firstname, lastname)

            if name == "Homer Simpson":
                password = md5_hash(HOMER_PASSWORD)
                is_admin = False
            elif name == "Charles Montgomery Burns":
                password = md5_hash(BURNS_PASSWORD)
                is_admin = True
            else:
                password = md5_hash(random_password())
                is_admin = False

            # Create UserCreate instance
            user_data = UserCreate(
                username=username,
                name=name,
                password=password,
                is_admin=is_admin
            )

            # Convert to SQLAlchemy User model
            user = User(**user_data.model_dump())
            users.append(user)

        # Add users to session and commit
        session.add_all(users)
        session.commit()
    finally:
        session.close()

if __name__ == "__main__":
    seed_users()
