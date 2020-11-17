from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class RegNumber(Base):
    __tablename__ = 'reg_number'

    CustomerID = sa.Column(sa.Integer, sa.ForeignKey('customer.CustomerID'), nullable=False),
    RegNumber = sa.Column(sa.String(45), nullable=False, primary_key=True),
    CarID = sa.Column(sa.Integer, sa.ForeignKey('car.CarID'), nullable=False)
    FkCarCustomer = relationship("Customer", back_populates="CustomerID")
    RegNumCarID = relationship("Car", back_populates="CarID")

    def __repr__(self):
        return f'{self.CustomerID}, {self.RegNumber}, {self.CarID}'

