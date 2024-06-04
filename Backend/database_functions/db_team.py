from Backend.database.models import Employee, TeamEmployee, Teams
from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


def check_team_name_duplicate(team_name: str, db: Session):
    team = db.query(Teams).filter(Teams.name == team_name).first()

    if team:
        return True
    else:
        return False


def create_team(team_name: str, db: Session):
    check = check_team_name_duplicate(team_name, db)

    if check:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='This Team Name Already Exists')

    team = Teams(
        name=team_name
    )

    db.add(team)
    db.commit()

    # members_id = db.query(TeamEmployee).filter(TeamEmployee.id == team.id).all()
    # members = []
    #
    # for ids in members_id:
    #     member = db.query(Employee).filter(Employee.id == ids.employee_id).first()
    #     members.append(member)
    #
    # result = {
    #     'id': team.id,
    #     'name': team.name,
    #     'number_of_members': team.number_of_members,
    #     'members': members
    # }

    return team


def delete_team(team_id: int, db: Session):
    team = db.query(Teams).filter(Teams.id == team_id).first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Team not found'
        )

    name = team.name

    team_employee = db.query(TeamEmployee).filter(TeamEmployee.team_id == team_id).all()

    for item in team_employee:
        db.delete(item)

    db.delete(team)
    db.commit()

    return f'{name} Team Deleted Successfully'


def add_team_member(team_id: int, employee_id: int, db: Session):
    team = db.query(Teams).filter(Teams.id == team_id).first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Team not found'
        )

    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    employee_team = db.query(TeamEmployee).filter(and_(TeamEmployee.team_id == team_id, TeamEmployee.employee_id == employee_id)).first()
    if employee_team:
        return f'{employee.first_name} {employee.last_name} is already a member of {team.name}'

    else:
        employee_team = TeamEmployee(
            employee_id=employee_id,
            team_id=team_id
        )

        team.number_of_members += 1
        db.add(employee_team)
        db.commit()

        return f'{employee.first_name} {employee.last_name} added to {team.name}'


def remove_team_member(team_id: int, employee_id: int, db: Session):
    team = db.query(Teams).filter(Teams.id == team_id).first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Team not found'
        )

    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee not found'
        )

    employee_team = db.query(TeamEmployee).filter(and_(TeamEmployee.team_id == team_id, TeamEmployee.employee_id == employee_id)).first()

    if employee_team:
        db.delete(employee_team)
        if team.number_of_members == 1:
            return delete_team(team_id, db)

        team.number_of_members -= 1
        db.commit()

        return f'{employee.first_name} {employee.last_name} removed from {team.name}'

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This Employee Is Not A Member of This Team'
        )


def get_team_members(team_id: int, db: Session):
    members = []
    team_employee = db.query(TeamEmployee).filter(TeamEmployee.team_id == team_id).all()

    for item in team_employee:
        member = db.query(Employee).filter(Employee.id == item.employee_id).first()
        members.append(member)

    if not members:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Team Has No Members'
        )

    return members


def get_all_teams(db: Session):
    teams = db.query(Teams).all()

    if not teams:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No Team Was Found'
        )

    return teams
