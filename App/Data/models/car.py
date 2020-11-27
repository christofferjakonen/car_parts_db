from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'cars'

    CarID = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    Model = sa.Column(sa.String(45), nullable=False)
    Brand = sa.Column(sa.String(45), nullable=False)
    Color = sa.Column(sa.String(45), nullable=False)
    ModelYear = sa.Column(sa.String(45))
    Car_RegNumber = relationship("RegNumber", back_populates="RegNumber_Car", cascade='all, delete-orphan')
    Car_CarHasPart = relationship("CarHasPart", back_populates="CarHasPart_Car", cascade='all, delete-orphan')

    def __repr__(self):
        return f'Car ID: {self.CarID}, Model:{self.Model}, Brand: {self.Brand}, Color: {self.Color}, Model Year: {self.ModelYear}'
