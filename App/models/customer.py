from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'

    CustomerID = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False),
    CustomerName = sa.Column(sa.String(255), nullable=False),
    Customer_RegNumber = relationship("RegNumber", back_populates="RegNumber_Customer")

    def __repr__(self):
        return f'{self.CustomerID}, {self.CustomerName}'
