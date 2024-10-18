# routers/__init__.py

from fastapi import APIRouter
from .auth_router import auth_router
from .employee_router import employee_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(employee_router)
