from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class SupplierHasPart(Base):
    __tablename__ = 'suppliers_have_parts'

    Supplier = sa.Column(sa.String(255), sa.ForeignKey('suppliers.SupplierName'), primary_key=True, nullable=False)
    ProductNumPart = sa.Column(sa.INTEGER, sa.ForeignKey('parts.ProductNum'), primary_key=True, nullable=False)
    SupplierHasPart_Supplier = relationship('Supplier', back_populates='Supplier_SupplierHasPart')
    SupplierHasPart_Part = relationship('Part', back_populates='Part_SupplierHasPart')

    def __repr__(self):
        return f'{self.Supplier}, {self.ProductNumPart}'