from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.schemas.schemas import AdminModel, TeamDisplay, UserAuth, HourlyLeaveDisplay, EmployeeModel, EmployeeDisplay, DailyLeaveDisplay
from Backend.database_functions import db_leave
from Backend.authentication.auth import get_current_admin
from typing import List

router = APIRouter(prefix='/leave', tags=['Leave'])


@router.post('/add_hourly_leave', response_model=HourlyLeaveDisplay)
def add_hourly_leave(employee_id: int, number_of_hours: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.add_hourly_leave(employee_id=employee_id, number_of_hours=number_of_hours, db=db)


@router.post('/add_daily_leave', response_model=DailyLeaveDisplay)
def add_daily_leave(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.add_daily_leave(employee_id=employee_id, db=db)


@router.delete('/delete_hourly_leave')
def delete_hourly_leave(leave_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.delete_hourly_leave(h_leave_id=leave_id, db=db)


@router.delete('/delete_daily_leave')
def delete_daily_leave(leave_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.delete_daily_leave(d_leave_id=leave_id, db=db)


@router.post('/last_hourly_leave', response_model=List[HourlyLeaveDisplay])
def last_n_hourly_leave(n: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.last_n_hourly_leave(n=n, db=db)


@router.post('/last_daily_leave', response_model=List[DailyLeaveDisplay])
def last_n_daily_leave(n: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.last_n_daily_leave(n=n, db=db)


@router.post('/employee_hourly_leave', response_model=List[HourlyLeaveDisplay])
def get_employee_hourly_leave(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.get_employee_hourly_leave(employee_id=employee_id, db=db)


@router.post('/employee_daily_leave', response_model=List[DailyLeaveDisplay])
def get_employee_daily_leave(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.get_employee_daily_leave(employee_id=employee_id, db=db)


@router.get('/all_hourly_leave', response_model=List[HourlyLeaveDisplay])
def get_all_hourly_leave(db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.get_all_hourly_leave(db=db)


@router.get('/all_daily_leave', response_model=List[DailyLeaveDisplay])
def get_all_daily_leave(db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_leave.get_all_daily_leave(db=db)

