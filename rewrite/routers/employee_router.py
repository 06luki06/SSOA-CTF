from fastapi import APIRouter, Request, Depends, Form, HTTPException, Body
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import User, Comment
from middleware.auth import ensure_authenticated, get_current_user
from pydantic import BaseModel


employee_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for comment submission
class CommentCreate(BaseModel):
    comment: str
    recipientId: str  # Changed from UUID to int

    class Config:
        orm_mode = True

# Existing CommentCreate Pydantic model here

@employee_router.get("/employee")
async def employee_profile(request: Request, user: User = Depends(ensure_authenticated)):
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "title": "Profile",
        "username": user.username
    })

@employee_router.get("/employee/{eid}")
async def employee_detail(
    request: Request,
    eid: int,  # Changed from UUID to int
    user: User = Depends(ensure_authenticated),
    db: Session = Depends(get_db)
):
    target_user = db.query(User).filter(User.id == eid).first()
    if not target_user or target_user.id == user.id:
        return RedirectResponse(url="/employee", status_code=302)
    return templates.TemplateResponse("employee.html", {
        "request": request,
        "title": "Employee Profile",
        "isAdmin": target_user.is_admin,
        "name": target_user.name,
        "eid": target_user.id  # No need to convert to string
    })

@employee_router.get("/employee/admin/{eid}")
async def employee_admin(
    request: Request,
    eid: int,  # Changed from UUID to int
    user: User = Depends(ensure_authenticated),
    db: Session = Depends(get_db)
):
    target_user = db.query(User).filter(User.id == eid).first()
    if not target_user or not target_user.is_admin:
        return RedirectResponse(url="/employee", status_code=302)
    return templates.TemplateResponse("employee.html", {
        "request": request,
        "title": "Admin Profile",
        "isAdmin": target_user.is_admin,
        "name": target_user.name,
        "eid": target_user.id  # No need to convert to string
    })

@employee_router.post("/employee/search")
async def employee_search(
    request: Request,
    employeeName: str = Form(...),
    user: User = Depends(ensure_authenticated),
    db: Session = Depends(get_db)
):
    target_user = db.query(User).filter(User.name.ilike(f"%{employeeName}%")).first()
    if not target_user:
        return RedirectResponse(url="/employee", status_code=302)
    target_user_id = target_user.id
    if target_user.is_admin:
        return RedirectResponse(url=f"/employee/admin/{target_user_id}", status_code=302)
    else:
        return RedirectResponse(url=f"/employee/{target_user_id}", status_code=302)

@employee_router.post("/comments")
async def add_comment(
    comment_data: CommentCreate = Body(...),
    user: User = Depends(ensure_authenticated),
    db: Session = Depends(get_db)
):
    new_comment = Comment(
        author_id=user.id,
        recipient_id=comment_data.recipientId,
        comment=comment_data.comment
    )
    db.add(new_comment)
    db.commit()
    return JSONResponse({"message": "Comment added"})


@employee_router.get("/comments/{recipient_id}")
async def get_comments(
        recipient_id: int,
        db: Session = Depends(get_db)
):
    # Query to fetch the recipient's name
    full_name_query = "SELECT name FROM nuclear.employees WHERE id = :recipient_id"
    full_name_result = db.execute(text(full_name_query), {"recipient_id": recipient_id}).fetchone()

    # Extract the actual name from the tuple
    full_name = full_name_result[0] if full_name_result else None

    # Query to fetch the comments
    comments_raw_query = "SELECT * FROM nuclear.comments WHERE recipient_id = :recipient_id"
    comments = db.execute(text(comments_raw_query), {"recipient_id": recipient_id}).fetchall()

    # Convert the result set to a list of dictionaries
    comments_list = [dict(row._mapping) for row in comments]

    # Prepare the final response
    result = {
        "name": full_name,
        "comments": comments_list
    }

    return JSONResponse(result)
