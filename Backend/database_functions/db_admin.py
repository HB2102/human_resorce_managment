from Backend.database.models import Admin
from sqlalchemy.orm import Session
from Backend.database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status
from Backend.schemas.schemas import AdminModel


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