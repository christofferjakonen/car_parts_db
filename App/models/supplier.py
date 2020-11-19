from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Supplier(Base):
    __tablename__ = 'suppliers'

    SupplierName = sa.Column(sa.String(100), primary_key=True, nullable=False)
    PhoneNumber = sa.Column(sa.String(45))
    Email = sa.Column(sa.String(100))
    Supplier_SupplierContactPerson = relationship('SupplierContactPerson', back_populates='SupplierContactPerson_Supplier')
    Supplier_SupplierHasManufacture = relationship('SupplierHasManufacture', back_populates='SupplierHasManufacture_Supplier')
    Supplier_SupplierHasPart = relationship('SupplierHasPart', back_populates='SupplierHasPart_Supplier')
    Supplier_SupplierAddress = relationship('SupplierAddress', back_populates='SupplierAddress_Supplier')

    def __repr__(self):
        return f'{self.SupplierName}, {self.PhoneNumber}, {self.Email}'
