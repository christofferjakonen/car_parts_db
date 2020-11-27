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
from sqlalchemy import delete, insert, update
from sqlalchemy.exc import SQLAlchemyError


def get_all_customers():
    return session.query(Customer).order_by(Customer.CustomerName).all()


def get_all_reg_numbers():


    return session.query(RegNumber).order_by(RegNumber.CustomerID).all()


def get_customer_by_id(id):
    return session.query(Customer).filter(Customer.CustomerID == id).first()


def get_customer_by_name(pattern):
    # Post.query.filter(Post.tags.like(search)).all()
    return session.query(Customer).filter(Customer.CustomerName.like(f'%{pattern}%')).all()


def store_changes():
    session.commit()


def store_new_customer(new_name):
    try:

        new_customer = Customer(CustomerName=new_name)
        session.add(new_customer)
        session.commit()
        session.close()
        print('done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def change_name(old_name, name):
    try:

        stmt1 = session.query(Customer).filter_by(CustomerName=old_name)
        stmt2 = {'CustomerName': name}

        stmt1.update(stmt2)
        session.commit()
        session.close()
        print('done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def delete_customer(id):
    try:
        del_cus = session.query(Customer).get(id)
        session.delete(del_cus)
        session.commit()
        session.close()
        print('done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def add_car_to_customer(cust_id, reg_num, car_id):

    try:
        new_reg_num = RegNumber(CustomerID=cust_id, RegNumber=reg_num, CarID=car_id)
        session.add(new_reg_num)
        session.commit()
        session.close()
        print('done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def delete_reg_num(reg_num):

    try:
        del_reg = session.query(RegNumber).get(reg_num)
        session.delete(del_reg)
        session.commit()
        session.close()
        print('done!')

    except SQLAlchemyError as error:

        print(error.__dict__["orig"])
        session.rollback()


def get_reg_number_for_customer(id):

    reg_num = session.query(RegNumber.RegNumber).filter(RegNumber.CustomerID == id).all()

    car_id = session.query(RegNumber.CarID).filter(RegNumber.CustomerID == id).all()

    return reg_num, car_id
