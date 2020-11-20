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



def get_all_cars():
    return session.query(Car).all()


def get_all_reg_numbers():
    return session.query(RegNumber).all()


def get_car_by_id(id):
    return session.query(Car).filter(Car.CarID == id).first()


def store_changes():
    session.commit()


def store_new_name(customer, new_value):
    try:
        customer.CustomerName = new_value
        # ....
        session.commit()
    except:
        session.rollback()
