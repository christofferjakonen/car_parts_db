"""fixed FK in car_has_parts

Revision ID: b9bd757b0da9
Revises: f4c90fb5d064
Create Date: 2020-11-25 15:50:10.660361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision = 'b9bd757b0da9'
down_revision = 'f4c90fb5d064'
branch_labels = None
depends_on = None


def upgrade():
    naming_convention = {
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

    with op.batch_alter_table("car_has_parts", naming_convention=naming_convention) as chp:
        chp.drop_constraint("car_has_parts_ibfk_1", type_="foreignkey")
        chp.create_foreign_key(
            "car_has_parts_ibfk_1",
            "cars",
            ["CarID"],
            ["CarID"])


def downgrade():
    naming_convention = {
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

    with op.batch_alter_table("car_has_parts", naming_convention=naming_convention) as chp:
        chp.drop_constraint("car_has_parts_ibfk_1", type_="foreignkey")
        chp.create_foreign_key(
            "car_has_parts_ibfk_1",
            "customers",
            ["CarID"],
            ["CustomerID"])