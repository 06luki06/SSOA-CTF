from fastapi import APIRouter, Request, Depends, Body, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.responses import RedirectResponse

from environment import NUKE_PIN
from middleware.auth import ensure_admin, ensure_authenticated
from utils import limiter
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

    print("admin chekc" + str(body))
    global check
    check = body
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "title": "Admin Portal",
        "username": user.username,
        "check_burns": check.burns,
        "check_mayor": check.mayor,
    })

@admin_router.get("/admin/nuke")
async def nuke_shelby_ville(
        request: Request,
        user: User = Depends(ensure_admin),
):
    global check

    if not check.burns or not check.mayor:
        return RedirectResponse(url="/admin", status_code=302)

    return templates.TemplateResponse("nuke.html", {
        "request": request,
        "title": "Nuclear Launch",
    })

@admin_router.post("/admin/nuke/pin")
@limiter.limit("5/minute")
async def start_nuke(
        request: Request,
        _user: User = Depends(ensure_authenticated),
        pin: str = Form(...),
):
    if pin != NUKE_PIN:
        return RedirectResponse(url="/admin/nuke", status_code=302)

    return templates.TemplateResponse("final.html", {
        "request": request,
    })