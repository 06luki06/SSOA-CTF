from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import User
from environment.config import HOMER_PASSWORD
from middleware.auth import get_current_user
import hashlib
import base64
import httpx

auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")

def md5_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()  # <-- add this for MD5 hashing

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

    if user:
        if user.password == md5_hash(password):
            request.session['user_id'] = user.id
            request.session['username'] = username
            request.session['password'] = password

            if user.is_admin:
                return RedirectResponse(url="/admin", status_code=302)
            else:
                return RedirectResponse(url="/employee", status_code=302)

    return templates.TemplateResponse("login.html", {
        "request": request,
        "title": "Login",
        "error": "Invalid credentials"
    })

@auth_router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)

@auth_router.post("/waste")
async def waste(
    request: Request,
    url: str = Form(...),
):
    token = base64.b64encode(f"hSimpson:{HOMER_PASSWORD}".encode()).decode()

    async with httpx.AsyncClient() as client:
        await client.post(url, headers={'Authorization': f'Basic {token}'})

    return RedirectResponse(url=request.url, status_code=204)