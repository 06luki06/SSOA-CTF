from fastapi import APIRouter, Request, Depends, Body
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from middleware.auth import ensure_admin
from validate import User

admin_router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Check(BaseModel):
    burns: bool = False
    mayor: bool = False


check = Check()

@admin_router.get("/admin")
async def login_page(
    request: Request,
    user: User = Depends(ensure_admin),
):
    print(check)
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "title": "Admin Portal",
        "username": user.username,
        "check_burns": check.burns,
        "check_mayor": check.mayor,
    })

@admin_router.post("/admin/check")
async def postCheck(
    request: Request,
    user: User = Depends(ensure_admin),
    body: Check = Body(...),
):
    global check
    check = body
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "title": "Admin Portal",
        "username": user.username,
        "check_burns": check.burns,
        "check_mayor": check.mayor,
    })
