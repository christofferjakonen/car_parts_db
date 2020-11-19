from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class SupplierHasManufacture(Base):
    __tablename__ = 'suppliers_have_manufacturers'

    Manufacture = sa.Column(sa.String(255), sa.ForeignKey('manufacturer.Manufacture'), primary_key=True, nullable=False)
    Supplier = sa.Column(sa.String(255), sa.ForeignKey('supplier.SupplierName'), primary_key=True, nullable=False)
    SupplierHasManufacture_Supplier = relationship('Supplier', back_populates='Supplier_SupplierHasManufacture')
    SupplierHasManufacture_Manufacture = relationship('Manufacture', back_populates='Manufacture_SupplierHasManufacture')

    def __repr__(self):
        return f'{self.Manufacture}, {self.Supplier}'
