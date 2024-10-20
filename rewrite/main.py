from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from routers import router
from database.connection import Base, engine
from environment.config import SECRET_KEY

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Mount static files
app.mount("/public", StaticFiles(directory="public"), name="public")

# Include routers
app.include_router(router)
