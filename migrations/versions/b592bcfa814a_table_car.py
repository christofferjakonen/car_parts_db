"""table car

Revision ID: b592bcfa814a
Revises: 6a5b14aa9b81
Create Date: 2020-11-16 15:12:37.647195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b592bcfa814a'
down_revision = '6a5b14aa9b81'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'car',
        sa.Column('CarID', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('Model', sa.String(45), nullable=False),
        sa.Column('Brand', sa.String(45), nullable=False),
        sa.Column('Color', sa.String(45), nullable=False),
        sa.Column('Model', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('car')