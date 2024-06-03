from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.schemas.schemas import UserAuth, HourlyLeaveDisplay, EmployeeModel, EmployeeDisplay, DailyLeaveDisplay
from Backend.database_functions import db_leave
from Backend.authentication.auth import get_current_admin
from typing import List

router = APIRouter(prefix='/arr_dep', tags=['Arrival and Departure'])

