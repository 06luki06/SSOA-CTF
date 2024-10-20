import os
from dotenv import load_dotenv

load_dotenv()

def get_req_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Environment variable {name} is not set")
    return value

# Database configuration
PG_HOST = get_req_env_var("PG_HOST")
PG_PORT = get_req_env_var("PG_PORT")
PG_DB = get_req_env_var("PG_DB")
PG_USER = get_req_env_var("PG_USER")
PG_PASSWORD = get_req_env_var("PG_PASSWORD")
PG_SCHEMA = get_req_env_var("PG_SCHEMA")

DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

# Secret key for session
SECRET_KEY = get_req_env_var("SECRET_KEY")

# Homer's credentials
HOMER_PASSWORD = get_req_env_var("HOMER_PASSWORD")

# Burns's credentials
BURNS_PASSWORD = get_req_env_var("BURNS_PASSWORD")
