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
    pass
    # with op.batch_alter_table("car_has_parts") as chp:
    #     chp.drop_constraint('car_has_parts_ibfk_1', type_='foreignkey')
    #     chp.create_foreign_key('car_has_parts_ibfk_1',  referent_table='cars', local_cols=['CarID'], remote_cols=['CarID'])
        #chp.drop_column("CarID"),
        #chp.add_column(sa.Column("CarID", sa.Integer, sa.ForeignKey("cars.CarID"), primary_key=True, nullable=False))


def downgrade():
    pass
    # with op.batch_alter_table("car_has_parts") as chp:
    #     chp.drop_column("CarID"),
    #     chp.add_column(sa.Column("CarID", sa.ForeignKey("customers.CustomerID"), primary_key=True, nullable=False))
