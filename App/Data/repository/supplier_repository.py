from Data.models.supplier import Supplier
from Data.models.supplier_contact_person import SupplierContactPerson
from Data.models.supplier_address import SupplierAddress
from Data.models.supplier_has_manufacture import SupplierHasManufacture
from Data.models.supplier_has_parts import SupplierHasPart
from Data.models.car import Car
from Data.models.car_has_parts import CarHasPart
from Data.models.customer import Customer
from Data.models.manufacture import Manufacture
from Data.models.manufacture_contact_person import ManufactureContactPerson
from Data.models.part import Part
from Data.models.reg_number import RegNumber
from Data.models.warehouse import Warehouse

from Data.db import session
import sqlalchemy

# supplier


def get_all_suppliers():
    return session.query(Supplier).all()


def add_new_supplier(supplier, phone_num, email):
    new_supplier = Supplier(SupplierName=supplier, PhoneNumber=phone_num, Email=email)
    session.add(new_supplier)
    session.commit()
    session.close()


def delete_supplier(supplier_name):
    d = session.query(Supplier).get(supplier_name)
    session.delete(d)
    session.commit()
    session.close()


def get_supplier_by_name(supplier_name):
    return session.query(Supplier).filter(Supplier.SupplierName.like(f'%{supplier_name}%')).all()


def get_supplier_by_phone_number(phone_num):
    return session.query(Supplier).filter(Supplier.PhoneNumber.like(f'%{phone_num}%')).all()


def get_supplier_by_email(email):
    return session.query(Supplier).filter(Supplier.Email.like(f'%{email}%')).all()


def store_edited_supplier_name(supplier, new_value):
    try:
        supplier.SupplierName = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_phone(supplier, new_value):
    try:
        supplier.PhoneNumber = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_email(supplier, new_value):
    try:
        supplier.Email = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


# contacts


def get_all_supplier_contact_people():
    return session.query(SupplierContactPerson).all()


def get_supplier_contact_person_by_name(contact_person):
    return session.query(SupplierContactPerson).filter(SupplierContactPerson.FullName.like(f'%{contact_person}%')).all()


def get_supplier_contact_person_by_phone_number(phone_num):
    return session.query(SupplierContactPerson).filter(SupplierContactPerson.PhoneNumber.like(f'%{phone_num}%')).all()


def get_supplier_contact_person_by_email(email):
    return session.query(SupplierContactPerson).filter(SupplierContactPerson.Email.like(f'%{email}%')).all()


def get_supplier_contact_person_by_supplier(supplier):
    return session.query(SupplierContactPerson).filter(SupplierContactPerson.Supplier.like(f'%{supplier}%')).all()


def add_new_supplier_contact(supplier, contact_name, phone_num, email):
    new_supplier_contact_person = SupplierContactPerson(Supplier=supplier, FullName=contact_name, PhoneNumber=phone_num, Email=email)
    session.add(new_supplier_contact_person)
    session.commit()
    session.close()


def delete_supplier_contact_person(contact_name):
    contact = session.query(SupplierContactPerson).get(contact_name)
    print(contact)
    print(type(contact))
    session.delete(contact)
    session.commit()
    session.close()


# addresses


def get_all_supplier_addresses():
    return session.query(SupplierAddress).all()


def get_supplier_address_by_name(supplier_name):
    return session.query(SupplierAddress).filter(SupplierAddress.Supplier.like(f'%{supplier_name}%')).all()


def get_supplier_address_by_country(country):
    return session.query(SupplierAddress).filter(SupplierAddress.Country.like(f'%{country}%')).all()


def get_supplier_address_by_city(city):
    return session.query(SupplierAddress).filter(SupplierAddress.City.like(f'%{city}%')).all()


def get_supplier_address_by_state(state):
    return session.query(SupplierAddress).filter(SupplierAddress.State.like(f'%{state}%')).all()


def get_supplier_address_by_zip_code(zip_code):
    return session.query(SupplierAddress).filter(SupplierAddress.ZipCode == zip_code).first()


def get_supplier_address_by_street_address(street_address):
    return session.query(SupplierAddress).filter(SupplierAddress.StreetAddress.like(f'%{street_address}%')).all()


def add_new_supplier_address(supplier, country, state, city, zip_code, street_address):
    new_supplier_contact_person = SupplierAddress(Supplier=supplier, Country=country, State=state, City=city, ZipCode=zip_code, SupplierAddress=street_address)
    session.add(new_supplier_contact_person)
    session.commit()
    session.close()


def store_edited_supplier_address_name(supplier_address, new_value):
    try:
        supplier_address.Supplier = new_value
        session.commit()
        session.close()
        print(supplier_address)
    except:
        session.rollback()


def store_edited_supplier_address_country(supplier_address, new_value):
    try:
        supplier_address.Country = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_address_state(supplier_address, new_value):
    try:
        supplier_address.State = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_address_city(supplier_address, new_value):
    try:
        supplier_address.City = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_address_zip_code(supplier_address, new_value):
    try:
        supplier_address.ZipCode = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def store_edited_supplier_address_street_address(supplier_address, new_value):
    try:
        supplier_address.StreetAddress = new_value
        session.commit()
        session.close()
    except:
        session.rollback()


def delete_supplier_address(supplier_name):
    d = session.query(SupplierAddress).get(supplier_name)
    session.delete(d)
    session.commit()
    session.close()


# manufacturers


def get_all_supplier_manufacturers():
    return session.query(SupplierHasManufacture).all()


# parts


def get_all_supplier_parts():
    return session.query(SupplierHasPart).all()
