import datetime

from pydantic import BaseModel
from fastapi import Query
from typing import Optional, List


class EmployeeModel(BaseModel):
    first_name: str
    last_name: str
    # email = Column(String)
    # phone_number = Column(String(20))
    # social_number = Column(String(20))
    # date_hired: datetime.datetime
    # position = Column(String(70))


class UpdateEmployeeModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]


class EmployeeDisplay(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class AdminModel(BaseModel):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


class AdminDisplay(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class PromoteToAdmin(BaseModel):
    username: str
    password: str


class TeamDisplay(BaseModel):
    id: int
    name: str
    number_of_members: int
    # members: List[EmployeeDisplay]

    class Config:
        from_attributes = True


class HourlyLeaveDisplay(BaseModel):
    employee_id: int
    number_of_hours: int
    date: datetime.datetime


class DailyLeaveDisplay(BaseModel):
    employee_id: int
    date: datetime.datetime

