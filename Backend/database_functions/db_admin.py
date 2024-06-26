from Backend.database.models import Admin, Employee
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from Backend.database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import AdminModel, PromoteToAdmin, UpdateEmployeeModel


def get_admin_by_username(username: str, db: Session):
    user = db.query(Admin).filter(Admin.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Admin not found!')

    return user


def create_admin(request: AdminModel, db: Session):
    username = request.username
    checked_duplicate = check_username_duplicate(username, db)

    if checked_duplicate:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='This username already exists')

    admin = Admin(
        username=request.username,
        password=Hash.bcrypt(request.password),
        first_name=request.first_name,
        last_name=request.last_name
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)

    return admin


def check_username_duplicate(username: str, db: Session):
    user = db.query(Admin).filter(Admin.username == username).first()

    if user:
        return True
    else:
        return False


def update_admin_self_info(admin_id: int, request: AdminModel, db: Session):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Admin not found'
        )

    if admin.username != request.username:
        checked = check_username_duplicate(request.username, db)
        if checked:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='This username already exists')

        admin.username = request.username

    admin.password = Hash.bcrypt(request.password)
    admin.first_name = request.first_name
    admin.last_name = request.last_name

    db.commit()

    return admin


def delete_self_admin(admin_id: int, db: Session):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Admin not found'
        )

    first_name = admin.first_name
    last_name = admin.last_name

    db.delete(admin)
    db.commit()

    return f"Admin Access of {first_name} {last_name} has benn deleted."


def promote_to_admin(request: PromoteToAdmin, employee_id: int, db: Session, admin_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    check = check_username_duplicate(request.username, db)
    if check:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='This username already exists')

    admin = Admin(
        first_name=employee.first_name,
        last_name=employee.last_name,
        username=request.username,
        password=Hash.bcrypt(request.password)
    )

    db.add(admin)
    db.commit()

    return admin


def search_user_by_name(request: UpdateEmployeeModel, db: Session, admin_id: int):
    results = []

    best_result = db.query(Employee).filter(and_(Employee.first_name == request.first_name, Employee.last_name == request.last_name)).all()

    for br in best_result:
        results.append(br)

    other_results = db.query(Employee).filter(or_(Employee.first_name == request.first_name, Employee.last_name == request.last_name)).all()

    for other_r in other_results:
        results.append(other_r)

    if not results:
        return "No result found for your search."

    return results


def exact_search_user_by_name(request: UpdateEmployeeModel, db: Session, admin_id: int):
    results = []

    best_result = db.query(Employee).filter(and_(Employee.first_name == request.first_name, Employee.last_name == request.last_name)).all()

    for br in best_result:
        results.append(br)

    if not results:
        return "No result found for your search."

    return results


def get_all_employees(db: Session):
    employees = db.query(Employee).all()

    if not employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Employee Found.'
        )

    return employees


