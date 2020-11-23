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


def get_all_parts():
    return session.query(Part).all()


def get_part_by_id(id):
    return session.query(Part).filter(Part.ProductNum == id).first()


"""

def get_customer_by_name(pattern):
    # Post.query.filter(Post.tags.like(search)).all()
    return session.query(Customer).filter(Customer.customerName.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_first_name(customer, new_value):
    try:
        customer.contactFirstName = new_value
        # ....
        session.commit()
    except:
        session.rollback()
"""
