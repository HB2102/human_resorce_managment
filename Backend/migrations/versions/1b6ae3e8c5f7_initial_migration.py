"""Initial migration

Revision ID: 1b6ae3e8c5f7
Revises: 
Create Date: 2024-06-04 11:46:36.324761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b6ae3e8c5f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_admin_id', table_name='admin')
    op.drop_table('admin')
    op.drop_index('ix_daily_leave_id', table_name='daily_leave')
    op.drop_table('daily_leave')
    op.drop_index('ix_team_id', table_name='team')
    op.drop_table('team')
    op.drop_index('ix_team_employee_id', table_name='team_employee')
    op.drop_table('team_employee')
    op.drop_index('ix_arrival_departure_id', table_name='arrival_departure')
    op.drop_table('arrival_departure')
    op.drop_index('ix_hourly_leave_id', table_name='hourly_leave')
    op.drop_table('hourly_leave')
    op.drop_index('ix_employee_id', table_name='employee')
    op.drop_table('employee')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_employee_id', 'employee', ['id'], unique=1)
    op.create_table('hourly_leave',
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('number_of_hours', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_hourly_leave_id', 'hourly_leave', ['id'], unique=1)
    op.create_table('arrival_departure',
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('arrival_or_departure', sa.BOOLEAN(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_arrival_departure_id', 'arrival_departure', ['id'], unique=1)
    op.create_table('team_employee',
    sa.Column('team_id', sa.INTEGER(), nullable=True),
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_team_employee_id', 'team_employee', ['id'], unique=1)
    op.create_table('team',
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('number_of_members', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('ix_team_id', 'team', ['id'], unique=1)
    op.create_table('daily_leave',
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_daily_leave_id', 'daily_leave', ['id'], unique=1)
    op.create_table('admin',
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index('ix_admin_id', 'admin', ['id'], unique=1)
    # ### end Alembic commands ###