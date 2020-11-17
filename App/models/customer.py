from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customer'

    CustomerID = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False),
    CustomerName = sa.Column(sa.String(255), nullable=False),
    FkCarCustomer = relationship("Reg_number", back_populates="FkCarCust")

    def __repr__(self):
        return f'{self.CustomerID}, {self.CustomerName}'
