import datetime
from Backend.database.models import Employee, ArrivalDeparture
from sqlalchemy import and_, desc
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


def add_arrival_departure(employee_id: int, kind: bool, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    ad = ArrivalDeparture(
        employee_id=employee_id,
        arrival_or_departure=kind,
        date=datetime.datetime.now()
    )

    db.add(ad)
    db.commit()

    return ad


def delete_arrival_departure(record_id: int, db: Session):
    record = db.query(ArrivalDeparture).filter(ArrivalDeparture.id == record_id).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Record not found'
        )

    db.delete(record)
    db.commit()

    return 'A_D Record Deleted Successfully'


def get_employee_last_n_arrival_or_departure(n: int, employee_id: int, kind: bool, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    if n < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Number You Put Is Not Acceptable"
        )

    records = db.query(ArrivalDeparture).filter(and_(ArrivalDeparture.employee_id == employee_id, ArrivalDeparture.arrival_or_departure == kind)).order_by(desc(ArrivalDeparture.date)).limit(n).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_employee_last_n_arrival_and_departure(n: int, employee_id:int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    if n < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Number You Put Is Not Acceptable"
        )

    records = db.query(ArrivalDeparture).filter(ArrivalDeparture.employee_id == employee_id).order_by(desc(ArrivalDeparture.date)).limit(n).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_employee_all_arrival_or_departure(employee_id: int, kind: bool, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    records = db.query(ArrivalDeparture).filter(and_(ArrivalDeparture.employee_id == employee_id, ArrivalDeparture.arrival_or_departure == kind)).order_by(desc(ArrivalDeparture.date)).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_employee_all_arrival_and_departure(employee_id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    records = db.query(ArrivalDeparture).filter(ArrivalDeparture.employee_id == employee_id).order_by(desc(ArrivalDeparture.date)).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_last_n_arrival_or_departure(n: int, kind: bool, db: Session):
    if n < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Number You Put Is Not Acceptable"
        )

    records = db.query(ArrivalDeparture).filter(ArrivalDeparture.arrival_or_departure == kind).order_by(desc(ArrivalDeparture.date)).limit(n).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_last_n_arrival_and_departure(n: int, db: Session):
    if n < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Number You Put Is Not Acceptable"
        )

    records = db.query(ArrivalDeparture).order_by(desc(ArrivalDeparture.date)).limit(n).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_all_arrival_or_departure(kind: bool, db: Session):
    records = db.query(ArrivalDeparture).filter(ArrivalDeparture.arrival_or_departure == kind).order_by(desc(ArrivalDeparture.date)).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records


def get_all_arrival_and_departure(db: Session):
    records = db.query(ArrivalDeparture).order_by(desc(ArrivalDeparture.date)).all()
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Record Found For Your Search'
        )

    return records

