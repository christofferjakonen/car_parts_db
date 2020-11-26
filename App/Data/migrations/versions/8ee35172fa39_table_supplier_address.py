"""table supplier_address

Revision ID: 8ee35172fa39
Revises: 68d4824f47dd
Create Date: 2020-11-16 15:14:28.768498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee35172fa39'
down_revision = '68d4824f47dd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'supplier_addresses',
        sa.Column('SupplierAddressID', sa.INTEGER, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('Supplier', sa.String(255), sa.ForeignKey('suppliers.SupplierName'), nullable=False),
        sa.Column('Country', sa.String(255), nullable=False),
        sa.Column('State', sa.String(255)),
        sa.Column('City', sa.String(255), nullable=False),
        sa.Column('ZipCode', sa.INTEGER, nullable=False),
        sa.Column('StreetAddress', sa.String(255), nullable=False)
    )


def downgrade():
    op.drop_table('supplier_addresses')
