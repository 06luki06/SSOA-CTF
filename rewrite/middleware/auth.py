from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get current user from session
def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user_id = int(user_id)  # Convert user_id to int
            return db.query(User).filter(User.id == user_id).first()
        except ValueError:
            # Handle invalid integer format
            return None
    return None

# Middleware equivalent to 'ensureAuthenticated'
def ensure_authenticated(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user
