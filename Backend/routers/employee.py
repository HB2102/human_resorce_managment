from fastapi import APIRouter, Depends, status
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.database.models import Employee
from Backend.schemas.schemas import EmployeeModel, UserAuth, EmployeeDisplay, UpdateEmployeeModel
from Backend.authentication.auth import get_current_admin
from Backend.database_functions import db_employee

router = APIRouter(prefix='/employee', tags=['Employee'])


@router.post('/add_employee', response_model=EmployeeDisplay)
def add_employee(request: EmployeeModel, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_employee.add_employee(request=request, db=db, admin_id=admin.id)


@router.delete('/delete_employee')
def delete_employee(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_employee.delete_employee(employee_id=employee_id, db=db, admin_id=admin.id)


@router.put('/update_employee', response_model=EmployeeDisplay)
def update_employee(employee_id: int, request: UpdateEmployeeModel, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_employee.update_employee_info(employee_id=employee_id, request=request, db=db, admin_id=admin.id)