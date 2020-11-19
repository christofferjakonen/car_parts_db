from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarHasParts(Base):
    __tablename__ = 'car_has_parts'

    CarID = sa.Column(sa.Integer, sa.ForeignKey('customer.CustomerID'), primary_key=True, nullable=False),
    PartsProductNum = sa.Column(sa.Integer, sa.ForeignKey('parts.ProductNum'), nullable=False, primary_key=True)
    FkCarID = relationship("Car", back_populates="CarID")
    CarHasParts_Part = relationship("Part", back_populates="Part_CarHasParts")
    CarHasParts_Car = relationship("Car", back_populates="Car_CarHasParts")


    def __repr__(self):
        return f'{self.CarID}, {self.PartsProductNum}'

