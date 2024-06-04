from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.database.models import Employee, Pictures
from Backend.schemas.schemas import UserAuth, URLDisplay
from Backend.authentication.auth import get_current_admin
from string import ascii_letters
import os
import random
import shutil

router = APIRouter(prefix='/picture', tags=['Picture'])


@router.post('/upload_pic')
def upload_employee_picture(employee_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f'_{rand_str}.'.join(file.filename.rsplit('.', 1))

    path_file = f'Backend/pictures/{new_name}'

    pic = db.query(Pictures).filter(Pictures.employee_id == employee_id).first()
    if pic:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='This Employee Already Has A Picture'
        )

    employee_picture = Pictures(
        employee_id=employee_id,
        pic_url=path_file,
    )

    db.add(employee_picture)
    db.commit()

    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return 'Picture Uploaded'


@router.delete('/delete_pic')
def delete_employee_picture(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    picture = db.query(Pictures).filter(Pictures.employee_id == employee_id).all()
    if not picture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No picture found !')

    if os.path.exists(picture.pic_url):
        os.remove(picture.pic_url)

    db.delete(picture)
    db.commit()

    return 'Employee picture deleted.'


@router.post('/get_pictures_of_employee', response_class=FileResponse)
def get_pictures_of_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee Not Found !"
        )

    picture = db.query(Pictures).filter(Pictures.employee_id == employee_id).first()
    if not picture:
        pic = 'Backend/pictures/default.jpg'
    else:
        pic = picture.pic_url

    return pic


@router.post('/url_picture_employee')
def get_pic_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee Not Found !"
        )

    picture = db.query(Pictures).filter(Pictures.employee_id == employee_id).first()
    if not picture:
        pic = 'Backend/pictures/default.jpg'
    else:
        pic = picture.pic_url

    return pic

