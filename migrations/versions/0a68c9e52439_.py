"""empty message

Revision ID: 0a68c9e52439
Revises: 
Create Date: 2017-05-24 09:31:30.800829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a68c9e52439'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_first_name'), 'employees', ['first_name'], unique=False)
    op.create_index(op.f('ix_employees_last_name'), 'employees', ['last_name'], unique=False)
    op.create_index(op.f('ix_employees_username'), 'employees', ['username'], unique=True)
    op.create_table('forecasts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('month', sa.String(length=15), nullable=True),
    sa.Column('hc', sa.Float(), nullable=True),
    sa.Column('month_hours', sa.Integer(), nullable=True),
    sa.Column('available', sa.Integer(), nullable=True),
    sa.Column('holiday', sa.Float(), nullable=True),
    sa.Column('holiday_percentage', sa.Float(), nullable=True),
    sa.Column('comp_percentage', sa.Float(), nullable=True),
    sa.Column('illness_percentage', sa.Float(), nullable=True),
    sa.Column('others_percentage', sa.Float(), nullable=True),
    sa.Column('vacation_percentage', sa.Float(), nullable=True),
    sa.Column('overtime_percentage', sa.Float(), nullable=True),
    sa.Column('education_percentage', sa.Float(), nullable=True),
    sa.Column('agent_holiday_eight', sa.Integer(), nullable=True),
    sa.Column('agent_holiday_ten', sa.Integer(), nullable=True),
    sa.Column('holiday_hours', sa.Integer(), nullable=True),
    sa.Column('compensation_hours', sa.Float(), nullable=True),
    sa.Column('illness_hours', sa.Float(), nullable=True),
    sa.Column('others_hours', sa.Float(), nullable=True),
    sa.Column('education_hours', sa.Float(), nullable=True),
    sa.Column('normal_hours', sa.Float(), nullable=True),
    sa.Column('overtime_hours', sa.Float(), nullable=True),
    sa.Column('agent_vacation_eight', sa.Integer(), nullable=True),
    sa.Column('agent_vacation_ten', sa.Integer(), nullable=True),
    sa.Column('vacation_hours', sa.Float(), nullable=True),
    sa.Column('hc_vacation', sa.Float(), nullable=True),
    sa.Column('chargeable', sa.Float(), nullable=True),
    sa.Column('utilization', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forecasts')
    op.drop_index(op.f('ix_employees_username'), table_name='employees')
    op.drop_index(op.f('ix_employees_last_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_first_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_table('employees')
    # ### end Alembic commands ###
