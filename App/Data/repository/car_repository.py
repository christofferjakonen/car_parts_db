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
from sqlalchemy import select, join


def get_all_cars():
    return session.query(Car).all()


def get_reg_number_for_car(id):
    reg_num = session.query(RegNumber.RegNumber).filter(RegNumber.CarID == id).all()

    cus_id = session.query(RegNumber.CustomerID).filter(RegNumber.CarID == id).all()

    return reg_num, cus_id


def view_parts_for_car_id(id):

    return session.query(CarHasPart.PartsProductNum).filter(CarHasPart.CarID == id).all()


def get_car_by_id(id):
    return session.query(Car).filter(Car.CarID == id).all()


def store_changes():
    session.commit()


def store_new_car(brand, model, color, model_year):
    try:

        new_car = Car(Brand=brand, Model=model, Color=color, ModelYear=model_year)
        session.add(new_car)
        session.commit()
        session.close()
        print('Done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def delete_car(id):
    try:
        del_car = session.query(Car).get(id)
        session.delete(del_car)
        session.commit()
        session.close()
        print('Done!')


    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()