from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.schemas.schemas import UserAuth, ArrivalDepartureDisplay
from Backend.database_functions import db_arrival_departure
from Backend.authentication.auth import get_current_admin
from typing import List

router = APIRouter(prefix='/arr_dep', tags=['Arrival and Departure'])


@router.post('/add_arrival_departure', response_model=ArrivalDepartureDisplay)
def add_arrival_departure(employee_id: int, kind: bool, db: Session = Depends(get_db)):
    return db_arrival_departure.add_arrival_departure(employee_id=employee_id, kind=kind, db=db)


@router.delete('/delete_arrival_departure')
def delete_arrival_departure(record_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.delete_arrival_departure(record_id=record_id, db=db)


@router.post('/employee_last_n_arrival_or_departure', response_model=List[ArrivalDepartureDisplay])
def employee_last_n_arrival_or_departure(employee_id: int, n: int, kind: bool, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_employee_last_n_arrival_or_departure(employee_id=employee_id, kind=kind, db=db, n=n)


@router.post('/employee_last_n_arrival_and_departure', response_model=List[ArrivalDepartureDisplay])
def employee_last_n_arrival_and_departure(employee_id: int, n: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_employee_last_n_arrival_and_departure(employee_id=employee_id, n=n, db=db)


@router.post('/employee_all_arrival_or_departure', response_model=List[ArrivalDepartureDisplay])
def get_employee_all_arrival_or_departure(employee_id: int, kind: bool, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_employee_all_arrival_or_departure(employee_id=employee_id,db=db,kind=kind)


@router.post('/employee_all_arrival_and_departure', response_model=List[ArrivalDepartureDisplay])
def get_employee_all_arrival_and_departure(employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_employee_all_arrival_and_departure(employee_id=employee_id, db=db)


@router.post('/last_n_arrival_or_departure', response_model=List[ArrivalDepartureDisplay])
def get_last_n_arrival_or_departure(kind: bool, n: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_last_n_arrival_or_departure(kind=kind, db=db, n=n)


@router.post('/last_n_arrival_and_departure', response_model=List[ArrivalDepartureDisplay])
def get_last_n_arrival_and_departure(n: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_last_n_arrival_and_departure(n=n, db=db)


@router.post('/all_arrival_or_departure', response_model=List[ArrivalDepartureDisplay])
def get_all_arrival_or_departure(kind: bool, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_all_arrival_or_departure(kind=kind, db=db)


@router.post('/all_arrival_and_departure', response_model=List[ArrivalDepartureDisplay])
def get_all_arrival_and_departure(db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_arrival_departure.get_all_arrival_and_departure(db=db)

