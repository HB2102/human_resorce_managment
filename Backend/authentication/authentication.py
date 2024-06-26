from fastapi import APIRouter, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from Backend.database import models
from Backend.database.database import get_db
from Backend.database.hash import Hash
from . import auth

router = APIRouter(tags=['Authentication'])


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Admin).filter(models.Admin.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid username')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')

    access_token = auth.create_access_token(data={'sub': user.username})

    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username,
    }
