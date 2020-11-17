from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Warehouse(Base):
    __tablename__ = 'warehouse'

    ProductNum = sa.Column(sa.Integer, sa.ForeignKey('parts.ProductNum'))
    Aisle = sa.Column(sa.String(45), primary_key=True, nullable=False)
    Bay = sa.Column(sa.String(45), primary_key=True, nullable=False)
    Shelf = sa.Column(sa.String(45), primary_key=True, nullable=False)
    AmountInStock = sa.Column(sa.Integer, nullable=False)
    MinAmount = sa.Column(sa.Integer)
    AutoBuyAmount = sa.Column(sa.Integer)
    ExpectedDeliveryDate = sa.Column(sa.DATE)

    FkProductNum = relationship('Part', back_populates="FkWarehouse")

    def __repr__(self):
        return f"{self.ProductNum}, {self.Aisle}, {self.Bay}, {self.Shelf}, {self.AmountInStock}, {self.MinAmount}, {self.AutoBuyAmount}, {self.ExpectedDeliveryDate}"