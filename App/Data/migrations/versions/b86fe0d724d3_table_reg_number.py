"""table reg_number

Revision ID: b86fe0d724d3
Revises: 3dd0af8e17c8
Create Date: 2020-11-16 15:15:39.694968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b86fe0d724d3'
down_revision = '3dd0af8e17c8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reg_numbers',
        sa.Column('CustomerID', sa.Integer, sa.ForeignKey('customers.CustomerID'), nullable=False),
        sa.Column('RegNumber', sa.String(45), nullable=False, primary_key=True),
        sa.Column('CarID', sa.Integer, sa.ForeignKey('cars.CarID'), nullable=False)
    )


def downgrade():
        op.drop_table('reg_numbers')
