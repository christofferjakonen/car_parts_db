from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ManufactureContactPerson(Base):
    __tablename__ = 'manufacture_contact_persons'

    Manufacture = sa.Column(sa.String(255), sa.ForeignKey('manufacturers.Manufacture'), nullable=False)
    FullName = sa.Column(sa.String(255), nullable=False)
    PhoneNumber = sa.Column(sa.String(50), primary_key=True, nullable=False)
    Email = sa.Column(sa.String(255), nullable=False)

    ManufactureContactPerson_Manufacture = relationship('Manufacture', back_populates="Manufacture_ManufactureContactPerson")

    def __repr__(self):
        return f"{self.Manufacture}, {self.FullName}, {self.PhoneNumber}, {self.Email}"
