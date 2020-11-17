"""table customer

Revision ID: 6a5b14aa9b81
Revises: 
Create Date: 2020-11-16 15:12:13.702230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a5b14aa9b81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('CustomerID', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('CustomerName', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('customer')
