"""table car_has_parts

Revision ID: 1e4ab07fef18
Revises: 2de5e0c8800a
Create Date: 2020-11-16 15:17:49.640759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e4ab07fef18'
down_revision = '2de5e0c8800a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'car_has_parts',
        sa.Column('CarID', sa.Integer, sa.ForeignKey('customer.CustomerID'), primary_key= True, nullable=False),
        sa.Column('PartsProductNum', sa.Integer, sa.ForeignKey('parts.ProductNum'), nullable=False, primary_key=True)
    )

def downgrade():
    op.drop_table('car_has_parts')
