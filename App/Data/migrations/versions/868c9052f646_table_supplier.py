"""table supplier

Revision ID: 868c9052f646
Revises: b592bcfa814a
Create Date: 2020-11-16 15:12:48.879265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '868c9052f646'
down_revision = 'b592bcfa814a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'suppliers',
        sa.Column('SupplierName', sa.String(100), primary_key=True, nullable=False),
        sa.Column('PhoneNumber', sa.String(45)),
        sa.Column('Email', sa.String(100))
    )


def downgrade():
    op.drop_table('suppliers')
