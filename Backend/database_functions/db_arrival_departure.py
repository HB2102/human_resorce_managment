import datetime
from Backend.database.models import Admin, Employee, TeamEmployee, Teams, HourlyLeave, DailyLeave
from sqlalchemy import and_, desc
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import EmployeeModel, AdminModel, UpdateEmployeeModel, TeamDisplay


def add_arrival_departure(employee_id: int, db: Session):
    pass


def delete_arrival_departure(record_id: int, db: Session):
    pass


def get_employee_last_n_arrival_or_departure(n: int, employee_id:int, db: Session):
    pass


def get_employee_last_n_arrival_and_departure(n: int, employee_id:int, db: Session):
    pass


def get_employee_all_arrival_or_departure(employee_id: int, db: Session):
    pass


def get_employee_all_arrival_and_departure(employee_id: int, db: Session):
    pass


def get_last_n_arrival_or_departure(n: int, db: Session):
    pass


def get_last_n_arrival_and_departure(n: int, db: Session):
    pass


def get_all_arrival_or_departure(n: int, db: Session):
    pass


def get_all_arrival_and_departure(n: int, db: Session):
    pass

