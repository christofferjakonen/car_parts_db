"""table supplier_has_manufacture

Revision ID: 68d4824f47dd
Revises: b49a672f6a2d
Create Date: 2020-11-16 15:14:20.264721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d4824f47dd'
down_revision = 'b49a672f6a2d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'supplier_has_manufacture',
        sa.Column('Manufacture', sa.String(255), sa.ForeignKey('manufacture.Manufacture'), primary_key=True, nullable=False),
        sa.Column('Supplier', sa.String(255), sa.ForeignKey('supplier.SupplierName'), primary_key=True, nullable=False)
    )


def downgrade():
    op.drop_table('supplier_has_manufacture')
