from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'car'

    CarID = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False),
    Model = sa.Column(sa.String(45), nullable=False),
    Brand = sa.Column(sa.String(45), nullable=False),
    Color = sa.Column(sa.String(45), nullable=False),
    ModelYear = sa.Column(sa.String(45))
    RegNumCar = relationship("Reg_number", back_populates="ReNuCaID")
    FkCarID = relationship("Car_has_parts", back_populates="RegNumCarID")

    def __repr__(self):
        return f'{self.CarID}, {self.Model}, {self.Brand}, {self.Color}, {self.ModelYear}'
