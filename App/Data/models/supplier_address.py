from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class SupplierAddress(Base):
    __tablename__ = 'supplier_addresses'

    SupplierAddressID = sa.Column(sa.INTEGER, primary_key=True, nullable=False, autoincrement=True)
    Supplier = sa.Column(sa.String(255), sa.ForeignKey('supplier.SupplierName'), nullable=False)
    Country = sa.Column(sa.String(255), nullable=False)
    State = sa.Column(sa.String(255))
    City = sa.Column(sa.String(255), nullable=False)
    ZipCode = sa.Column(sa.INTEGER, nullable=False)
    StreetAddress = sa.Column(sa.String(255), nullable=False)
    SupplierAddress_Supplier = relationship('Supplier', back_populates='Supplier_SupplierAddress')

    def __repr__(self):
        return f'{self.SupplierAddressID}, {self.Supplier}, {self.Country}, {self.State}, {self.City}, {self.ZipCode}, {self.StreetAddress}'
