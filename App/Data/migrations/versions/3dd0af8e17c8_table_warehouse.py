"""table warehouse

Revision ID: 3dd0af8e17c8
Revises: 6bd22495c77d
Create Date: 2020-11-16 15:15:27.173275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dd0af8e17c8'
down_revision = '6bd22495c77d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'warehouses',
        sa.Column('ProductNum', sa.Integer, sa.ForeignKey('parts.ProductNum')),
        sa.Column('Aisle', sa.String(45), primary_key=True, nullable=False),
        sa.Column('Bay', sa.String(45), primary_key=True, nullable=False),
        sa.Column('Shelf', sa.String(45), primary_key=True, nullable=False),
        sa.Column('AmountInStock', sa.Integer, nullable=False),
        sa.Column('MinAmount', sa.Integer),
        sa.Column('AutoBuyAmount', sa.Integer),
        sa.Column('ExpectedDeliveryDate', sa.DATE)
    )


def downgrade():
    op.drop_table('warehouses')
