from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class SupplierContactPerson(Base):
    __tablename__ = 'supplier_contact_people'

    Supplier = sa.Column(sa.String(255), sa.ForeignKey('supplier.SupplierName'), nullable=False)
    FullName = sa.Column(sa.String(255), nullable=False)
    PhoneNumber = sa.Column(sa.String(50), primary_key=True, nullable=False)
    Email = sa.Column(sa.String(255), nullable=False)
    SupplierContactPerson_Supplier = relationship('Supplier', back_populates='Supplier_SupplierContactPerson')

    def __repr__(self):
        return f'{self.Supplier}, {self.FullName}, {self.PhoneNumber}, {self.Email}'
