"""rename manufacture_contact_persons

Revision ID: f4c90fb5d064
Revises: 1e4ab07fef18
Create Date: 2020-11-23 10:15:04.636867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c90fb5d064'
down_revision = '1e4ab07fef18'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('manufacture_contact_person', 'manufacture_contact_persons')


def downgrade():
    op.rename_table('manufacture_contact_persons', 'manufacture_contact_person')
