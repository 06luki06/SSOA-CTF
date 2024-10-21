from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import PlainTextResponse

from routers import router
from database.connection import Base, engine
from environment.config import SECRET_KEY
from utils.rate_limiter import limiter

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)
app.include_router(router)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Add exception handler for rate limit exceeded
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return PlainTextResponse("Rate limit exceeded", status_code=429)


# Mount static files
app.mount("/public", StaticFiles(directory="public"), name="public")

# Include routers
app.include_router(router)
