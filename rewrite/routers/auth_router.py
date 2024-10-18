# routers/auth_router.py

from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from database import SessionLocal
from models import User
from middleware.auth import get_current_user
from config import HOMER_USERNAME, HOMER_PASSWORD
import base64
import httpx

auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.get("/")
async def index(
    request: Request,
    user: User = Depends(get_current_user)
):
    if not user:
        return RedirectResponse(url="/login")
    else:
        return RedirectResponse(url="/employee")

@auth_router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request,
        "title": "Nuclear Power Plant Login"
    })

@auth_router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt.verify(password, user.password):
        request.session['user_id'] = user.id  # No need to convert to string
        return RedirectResponse(url="/employee", status_code=302)
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "title": "Login",
            "error": "Invalid credentials"
        })

@auth_router.post("/logout")
async def logout(request: Request):
    request.session.pop('user_id', None)
    return RedirectResponse(url="/login", status_code=302)

@auth_router.post("/waste")
async def waste(
    request: Request,
    url: str = Form(...)
):
    # Base64 encode Homer's username and password
    token = base64.b64encode(f"{HOMER_USERNAME}:{HOMER_PASSWORD}".encode()).decode()
    # Make a POST request with Basic Auth
    async with httpx.AsyncClient() as client:
        await client.post(url, headers={'Authorization': f'Basic {token}'})
    return RedirectResponse(url="/login", status_code=302)
