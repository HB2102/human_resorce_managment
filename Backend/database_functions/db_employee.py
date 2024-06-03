from Backend.database.models import Admin, Employee
from sqlalchemy.orm import Session
from Backend.database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import EmployeeModel, AdminModel


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
    try:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Employee not found'
            )

        db.delete(employee)
        db.commit()

        return 'Employee Deleted'

    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrong!'
        )
