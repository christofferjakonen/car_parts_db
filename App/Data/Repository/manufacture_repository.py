
from Data.db import session
from Data.models.car import Car
from Data.models.car_has_parts import CarHasPart
from Data.models.customer import Customer
from Data.models.manufacture import Manufacture
from Data.models.manufacture_contact_person import ManufactureContactPerson
from Data.models.part import Part
from Data.models.reg_number import RegNumber
from Data.models.supplier import Supplier
from Data.models.supplier_address import SupplierAddress
from Data.models.supplier_contact_person import SupplierContactPerson
from Data.models.supplier_has_manufacture import SupplierHasManufacture
from Data.models.supplier_has_parts import SupplierHasPart
from Data.models.warehouse import Warehouse
from sqlalchemy.exc import SQLAlchemyError


def get_all_manufacturers():
    return session.query(Manufacture).all()


def add_new_manufacturer(manufacturer, country="None", state="None", city="None", zip=1, address="None", phone="None"):
    try:
        print("-- entering add_new_manufacturer --")
        newManufacturer = Manufacture(Manufacture=manufacturer, Country=country, State=state, City=city, ZipCode=zip, StreetAddress=address, PhoneNumber=phone)
        print("-- created new manufacturer --")
        session.add(newManufacturer)
        print("-- added new manufacturer to session --")
        session.commit()
        session.close()
    except SQLAlchemyError as error:
        print(error.__dict__["orig"])
        session.rollback()


def update_part_by_ID(manufacturer, columnName, newValue=None):
    try:
        stmt1 = session.query(Manufacture).filter_by(Manufacture=manufacturer)
        print(stmt1)
        stmt2 = {columnName: newValue}
        stmt1.update(stmt2)

        session.commit()
        session.close()
    except SQLAlchemyError as error:
        print(error.__dict__["orig"])
        session.rollback()

