from fastapi import APIRouter, Depends, status
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.database.models import Admin
from Backend.schemas.schemas import AdminModel, AdminDisplay
from Backend.database_functions import db_admin

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.post('/add_admin', response_model=AdminDisplay)
def add_admin(request: AdminModel, db: Session = Depends(get_db)):
    return db_admin.create_admin(request=request, db=db)
