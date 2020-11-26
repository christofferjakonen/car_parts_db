from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarHasPart(Base):
    __tablename__ = 'car_has_parts'

    CarID = sa.Column(sa.Integer, sa.ForeignKey('cars.CarID', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False)
    PartsProductNum = sa.Column(sa.Integer, sa.ForeignKey('parts.ProductNum'), nullable=False, primary_key=True)
    CarHasPart_Part = relationship("Part", back_populates="Part_CarHasPart")
    CarHasPart_Car = relationship("Car", back_populates="Car_CarHasPart")

    def __repr__(self):
        return f'{self.CarID}, {self.PartsProductNum}'