"""table manufacture_contact_person

Revision ID: b49a672f6a2d
Revises: 79c0660597b8
Create Date: 2020-11-16 15:13:34.810413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b49a672f6a2d'
down_revision = '79c0660597b8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacture_contact_person',
        sa.Column('Manufacture', sa.String(255), sa.ForeignKey('manufacturers.Manufacture'), nullable=False),
        sa.Column('FullName', sa.String(255), nullable=False),
        sa.Column('PhoneNumber', sa.String(50), primary_key=True, nullable=False),
        sa.Column('Email', sa.String(255), nullable=False)
    )


def downgrade():
    op.drop_table('manufacture_contact_person')