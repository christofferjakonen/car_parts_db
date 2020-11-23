"""table supplier_has_parts

Revision ID: 2de5e0c8800a
Revises: b86fe0d724d3
Create Date: 2020-11-16 15:17:35.685538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2de5e0c8800a'
down_revision = 'b86fe0d724d3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'supplier_has_parts',
        sa.Column('Supplier', sa.String(255), sa.ForeignKey('suppliers.SupplierName'), primary_key=True, nullable=False),
        sa.Column('ProductNumPart', sa.INTEGER, sa.ForeignKey('parts.ProductNum'), primary_key=True, nullable=False)
    )


def downgrade():
    op.drop_table('supplier_has_parts')
