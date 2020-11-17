from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Part(Base):
    __tablename__ = 'parts'

    ProductNum = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    Manufacture = sa.Column(sa.String(255), sa.ForeignKey('manufacturer.Manufacture'), nullable=False)
    ProductName = sa.Column(sa.String(100), nullable=False)
    PurchasePrice = sa.Column(sa.String(45), nullable=False)
    SellPrice = sa.Column(sa.String(45), nullable=False)
    PartDescription = sa.Column(sa.String(1000))
    Maker = relationship("Manufacturer", back_populates="Parts")

    def __repr__(self):
        return f'{self.ProductNum}, {self.Manufacture}, {self.ProductName}, {self.PurchasePrice}, {self.SellPrice}, {self.PartDescription}, {self.Maker}'
