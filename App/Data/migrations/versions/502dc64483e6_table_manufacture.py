"""table manufacture

Revision ID: 502dc64483e6
Revises: 868c9052f646
Create Date: 2020-11-16 15:12:57.660816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '502dc64483e6'
down_revision = '868c9052f646'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturer',
        sa.Column('Manufacture', sa.String(255), primary_key=True),
        sa.Column('Country', sa.String(100), nullable=False),
        sa.Column('State', sa.String(255)),
        sa.Column('City', sa.String(100), nullable=False),
        sa.Column('ZipCode', sa.Integer, nullable=False),
        sa.Column('StreetAddress', sa.String(255), nullable=False),
        sa.Column('PhoneNumber', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('manufacturer')