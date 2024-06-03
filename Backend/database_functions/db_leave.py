import datetime
from Backend.database.models import Admin, Employee, TeamEmployee, Teams, HourlyLeave, DailyLeave
from sqlalchemy import and_, desc
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import EmployeeModel, AdminModel, UpdateEmployeeModel, TeamDisplay


def add_hourly_leave(employee_id: int, number_of_hours: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    hourly_leave = HourlyLeave(
        employee_id=employee_id,
        number_of_hours=number_of_hours,
        date=datetime.datetime.today()
    )

    db.add(hourly_leave)
    db.commit()

    return hourly_leave


def add_daily_leave(employee_id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    daily_leave = DailyLeave(
        employee_id=employee_id,
        date=datetime.datetime.today()
    )

    db.add(daily_leave)
    db.commit()

    return daily_leave


def delete_hourly_leave(h_leave_id: int, db: Session):
    leave = db.query(HourlyLeave).filter(HourlyLeave.id == h_leave_id).first()

    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Leave Record Not Found'
        )

    db.delete(leave)
    db.commit()

    return "Leave Record Deleted Successfully"


def delete_daily_leave(d_leave_id: int, db: Session):
    leave = db.query(DailyLeave).filter(DailyLeave.id == d_leave_id).first()

    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Leave Record Not Found'
        )

    db.delete(leave)
    db.commit()

    return "Leave Record Deleted Successfully"


def last_n_hourly_leave(n: int, db: Session):
    leaves = db.query(HourlyLeave).order_by(desc(HourlyLeave.date)).limit(n).all()

    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found'
        )

    return leaves


def last_n_daily_leave(n: int, db: Session):
    leaves = db.query(DailyLeave).order_by(desc(DailyLeave.date)).limit(n).all()

    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found'
        )

    return leaves


def get_employee_hourly_leave(employee_id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    leaves = db.query(HourlyLeave).filter(HourlyLeave.employee_id == employee_id).order_by(desc(HourlyLeave.date)).all()
    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found For This Employee'
        )

    return leaves


def get_employee_daily_leave(employee_id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    leaves = db.query(DailyLeave).filter(DailyLeave.employee_id == employee_id).order_by(desc(DailyLeave.date)).all()
    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found For This Employee'
        )

    return leaves


def get_all_hourly_leave(db: Session):
    leaves = db.query(HourlyLeave).order_by(desc(HourlyLeave.date)).all()

    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found'
        )

    return leaves


def get_all_daily_leave(db: Session):
    leaves = db.query(DailyLeave).order_by(desc(DailyLeave.date)).all()

    if not leaves:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Leave Record Was Found'
        )

    return leaves


