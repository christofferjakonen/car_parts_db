"""table parts

Revision ID: 79c0660597b8
Revises: 502dc64483e6
Create Date: 2020-11-16 15:13:08.447661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79c0660597b8'
down_revision = '502dc64483e6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'parts',
        sa.Column('ProductNum', sa.Integer, primary_key=True, autoincrement=False),
        sa.Column('Manufacture', sa.String(255), sa.ForeignKey('manufacturer.Manufacture'), nullable=False),
        sa.Column('ProductName', sa.String(100), nullable=False),
        sa.Column('PurchasePrise', sa.String(45), nullable=False),
        sa.Column('SellPrice', sa.String(45), nullable=False),
        sa.Column('PartDescription', sa.String(1000))
    )


def downgrade():
    op.drop_table('parts')
