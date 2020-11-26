"""table supplier_contact_person'

Revision ID: 6bd22495c77d
Revises: 8ee35172fa39
Create Date: 2020-11-16 15:14:43.695734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bd22495c77d'
down_revision = '8ee35172fa39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'supplier_contact_persons',
        sa.Column('Supplier', sa.String(255), sa.ForeignKey('suppliers.SupplierName'), nullable=False),
        sa.Column('FullName', sa.String(255), nullable=False),
        sa.Column('PhoneNumber', sa.String(50), primary_key=True, nullable=False),
        sa.Column('Email', sa.String(255), nullable=False)
    )


def downgrade():
    op.drop_table('supplier_contact_persons')
