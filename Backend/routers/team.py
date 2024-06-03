from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from Backend.database.database import get_db
from Backend.schemas.schemas import AdminModel, TeamDisplay, UserAuth, PromoteToAdmin, EmployeeModel, EmployeeDisplay
from Backend.database_functions import db_team
from Backend.authentication.auth import get_current_admin
from typing import List

router = APIRouter(prefix='/team', tags=['Team'])


@router.post('/create_team', response_model=TeamDisplay)
def create_team(team_name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.create_team(db=db, team_name=team_name)


@router.delete('/delete_team')
def delete_team(team_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.delete_team(team_id=team_id, db=db)


@router.post('/add_employee')
def add_member(team_id: int, employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.add_team_member(team_id=team_id, employee_id=employee_id, db=db)


@router.delete('/remove_member')
def remove_member(team_id: int, employee_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.remove_team_member(team_id=team_id, employee_id=employee_id, db=db)


@router.post('/get_members', response_model=List[EmployeeDisplay])
def get_members(team_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.get_team_members(team_id=team_id, db=db)


@router.get('/all_teams', response_model=List[TeamDisplay])
def get_all_teams(db: Session = Depends(get_db), admin: UserAuth = Depends(get_current_admin)):
    return db_team.get_all_teams(db=db)

