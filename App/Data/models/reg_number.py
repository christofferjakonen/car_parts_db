from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class RegNumber(Base):
    __tablename__ = 'reg_numbers'

    CustomerID = sa.Column(sa.Integer, sa.ForeignKey('customers.CustomerID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    RegNumber = sa.Column(sa.String(45), nullable=False, primary_key=True)
    CarID = sa.Column(sa.Integer, sa.ForeignKey('cars.CarID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    RegNumber_Customer = relationship("Customer", back_populates="Customer_RegNumber")
    RegNumber_Car = relationship("Car", back_populates="Car_RegNumber")

    def __repr__(self):
        return f'Customer ID: {self.CustomerID}, Registration Number: {self.RegNumber}, Car ID: {self.CarID}'
