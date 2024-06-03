from Backend.database.models import Admin
from sqlalchemy.orm import Session
from Backend.database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def get_admin_by_username(username: str, db: Session):
    user = db.query(Admin).filter(Admin.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Admin not found !')

    return user