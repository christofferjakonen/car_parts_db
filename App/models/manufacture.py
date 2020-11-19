from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Manufacture(Base):
    __tablename__ = 'manufacturers'

    Manufacture = sa.Column(sa.String(255), primary_key=True)
    Country = sa.Column(sa.String(100), nullable=False)
    State = sa.Column(sa.String(255))
    City = sa.Column(sa.String(100), nullable=False)
    ZipCode = sa.Column(sa.Integer, nullable=False)
    StreetAddress = sa.Column(sa.String(255), nullable=False)
    PhoneNumber = sa.Column(sa.String(45), nullable=False)
    SparePart = relationship("Parts", back_populates="Manufacturer")

    def __repr__(self):
        return f'{self.Manufacture}, {self.Country}, {self.State}, {self.City}, {self.ZipCode}, {self.StreetAddress}, {self.PhoneNumber}, {self.SparePart}'
