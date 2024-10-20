from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from database.connection import get_db

auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")



@auth_router.get("/admin")
async def login_page(request: Request):
    db = get_db()
    return templates.TemplateResponse("login.html", {
        "request": request,
        "title": "Nuclear Power Plant Login"
    })
