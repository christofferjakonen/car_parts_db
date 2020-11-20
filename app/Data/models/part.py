from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Part(Base):
    __tablename__ = 'parts'

    ProductNum = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    Manufacture = sa.Column(sa.String(255), sa.ForeignKey('manufacturers.Manufacture'), nullable=False)
    ProductName = sa.Column(sa.String(100), nullable=False)
    PurchasePrice = sa.Column(sa.String(45), nullable=False)
    SellPrice = sa.Column(sa.String(45), nullable=False)
    PartDescription = sa.Column(sa.String(1000))

    Part_Manufacture = relationship("Manufacture", back_populates="Manufacture_Part")
    Part_Warehouse = relationship('Warehouse', back_populates="Warehouse_Part")
    Part_CarHasPart = relationship('CarHasPart', back_populates="CarHasPart_Part")
    Part_SupplierHasPart = relationship('SupplierHasPart', back_populates="SupplierHasPart_Part")


    def __repr__(self):
        return f'{self.ProductNum}, {self.Manufacture}, {self.ProductName}, {self.PurchasePrice}, {self.SellPrice}, {self.PartDescription}'
