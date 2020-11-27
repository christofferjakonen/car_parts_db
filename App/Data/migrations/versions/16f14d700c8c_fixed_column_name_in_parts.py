"""fixed column name in parts

Revision ID: 16f14d700c8c
Revises: f4c90fb5d064
Create Date: 2020-11-23 13:17:13.622241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16f14d700c8c'
down_revision = 'f4c90fb5d064'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("parts") as parts:
        parts.add_column(sa.Column("PurchasePrice", sa.String(45), nullable=False))
        parts.drop_column("PurchasePrise")

def downgrade():
    with op.batch_alter_table("parts") as parts:
        parts.add_column(sa.Column("PurchasePrise", sa.String(45), nullable=False))
        parts.drop_column("PurchasePrice")
