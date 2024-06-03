from Backend.database.models import Admin, Employee, TeamEmployee, Teams
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import EmployeeModel, AdminModel, UpdateEmployeeModel
from .db_team import remove_team_member


def add_employee(request: EmployeeModel, db: Session, admin_id: int):
    try:
        employee = Employee(
            first_name=request.first_name,
            last_name=request.last_name,
            # email=request.email,
            # phone_number=request.phone_number,
            # position=request.position,
            # social_number=request.social_number,
            # date_hired=request.date_hired
        )

        db.add(employee)
        db.commit()

        return employee

    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrong!'
        )


def delete_employee(employee_id: int, db: Session, admin_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    team_employee = db.query(TeamEmployee).filter(TeamEmployee.employee_id == employee_id).all()

    for item in team_employee:
        team_id = item.team_id
        remove_team_member(team_id, employee_id, db)

    db.delete(employee)
    db.commit()

    return 'Employee Deleted'


def update_employee_info(employee_id: int, request: UpdateEmployeeModel, db: Session, admin_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    employee.first_name = request.first_name
    employee.last_name = request.last_name

    db.commit()

    return employee





