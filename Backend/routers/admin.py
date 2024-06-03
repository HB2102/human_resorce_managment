from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.schemas.schemas import AdminModel, AdminDisplay, UserAuth, PromoteToAdmin
from Backend.database_functions import db_admin
from Backend.authentication.auth import get_current_admin

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.post('/add_admin', response_model=AdminDisplay)
def add_admin(request: AdminModel, db: Session = Depends(get_db)):
    return db_admin.create_admin(request=request, db=db)


@router.put('/update_admin', response_model=AdminDisplay)
def update_admin(request: AdminModel, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_admin.update_admin_self_info(request=request, db=db, admin_id=admin.id)


@router.delete('/delete_admin')
def delete_admin(db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_admin.delete_self_admin(db=db, admin_id=admin.id)


@router.put('promote_to_admin', response_model=AdminDisplay)
def promote_user(request: PromoteToAdmin, employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_admin.promote_to_admin(request=request, db=db, employee_id=employee_id, admin_id=admin.id)



