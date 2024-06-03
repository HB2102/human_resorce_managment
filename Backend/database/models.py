from Backend.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float


# ID Class ==================================================================================================
class ID:
    id = Column(Integer, unique=True, index=True, primary_key=True)


# EMPLOYEE TABLE ============================================================================================
class Employee(Base, ID):
    __tablename__ = 'employee'
    first_name = Column(String)
    last_name = Column(String)
    # email = Column(String)
    # phone_number = Column(String(20))
    # social_number = Column(String(20))
    # date_hired = Column(DateTime)
    # position = Column(String(70))


# EMPLOYEE TABLE ============================================================================================
class Teams(Base, ID):
    __tablename__ = 'team'
    name = Column(String, unique=True)
    number_of_members = Column(Integer, default=0)


# EMPLOYEE-Team TABLE =======================================================================================
class TeamEmployee(Base, ID):
    __tablename__ = 'team_employee'
    team_id = Column(Integer, ForeignKey('team.id'))
    employee_id = Column(Integer, ForeignKey('employee.id'))


# HOURY LEAVE TABLE ===============================================================================================
class HourlyLeave(Base, ID):
    __tablename__ = 'hourly_leave'
    employee_id = Column(Integer, ForeignKey('employee.id'))
    date = Column(DateTime)
    number_of_hours = Column(Integer)


# DAILY LEAVE TABLE =========================================================================================
class DailyLeave(Base, ID):
    __tablename__ = 'daily_leave'
    employee_id = Column(Integer, ForeignKey('employee.id'))
    date = Column(DateTime)


# Arrivals and Departures TABLE =============================================================================
class ArrivalDeparture(Base,ID):
    __tablename__ = 'arrival_departure'
    employee_id = Column(Integer, ForeignKey('employee.id'))
    date = Column(DateTime)
    arrival_or_departure = Column(Boolean)


# ADMIN TABLE ===============================================================================================
class Admin(Base,ID):
    __tablename__ = 'admin'
    username = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    # email = Column(String)
    # phone_number = Column(String(20))
    # is_super_admin = Column(Boolean)

