from Data.db import session
from sqlalchemy.sql.expression import delete
from Data.models.car import Car
from Data.models.car_has_parts import CarHasPart
from Data.models.customer import Customer
from Data.models.manufacture import Manufacture
from Controllers.manufacture_controller import add_new_manufacturer
from Data.models.manufacture_contact_person import ManufactureContactPerson
from Data.models.part import Part
from Data.models.reg_number import RegNumber
from Data.models.supplier import Supplier
from Data.models.supplier_address import SupplierAddress
from Data.models.supplier_contact_person import SupplierContactPerson
from Data.models.supplier_has_manufacture import SupplierHasManufacture
from Data.models.supplier_has_parts import SupplierHasPart
from Data.models.warehouse import Warehouse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError



def get_all_parts():
    return session.query(Part).order_by(Part.ProductNum).all()


def get_part_by_id(inputID):
    return session.query(Part).filter(Part.ProductNum == inputID).first()


def get_part_by_name(partName):
    return session.query(Part).filter(Part.ProductName.like(f"%{partName}%")).all()


def add_new_part(partID, partName=None, partMaker=None, description=None, cost=None, sellPrice=None):
    try:
        maker = session.query(Manufacture).filter(Manufacture.Manufacture == partMaker).first()
        if not maker:
            print("Manufacturer not found")
            answer = input("Add new manufacture as a blank manufacturer? (y/n): ")
            if answer == "y" or answer == "Y":
                # call function to create manufacture
                add_new_manufacturer(partMaker)
                maker = session.query(Manufacture).filter(Manufacture.Manufacture == partMaker).first()
            else:
                return None
        newPart = Part(ProductNum=partID, Manufacture=maker.Manufacture, ProductName=partName, PartDescription=description, PurchasePrice=cost, SellPrice=sellPrice)
        session.add(newPart)
        session.commit()
        session.close()
    except SQLAlchemyError as error:
        print(error.__dict__["orig"])
        session.rollback()


def update_part_by_ID(partID, columnName, newValue=None):
    try:
        stmt1 = session.query(Part).filter_by(ProductNum=partID)
        stmt2 = {columnName: newValue}
        try:
            stmt1.update(stmt2)
        except IntegrityError:
            print("\nUnknown manufacturer")
            print("Create new manufacture?")
            answer = input("y/n : ")
            if answer == "y" or answer == "Y":
                # create new manufacturer
                pass
            else:
                session.rollback()

        session.commit()
        session.close()
    except SQLAlchemyError as error:
        print(error.__dict__["orig"])
        session.rollback()


def delete_part_by_ID(command):
    try:
        stmt = session.query(Part).get(command)
        session.delete(stmt)
        session.commit()
        session.close()
    except SQLAlchemyError as error:
        print(error.__dict__["orig"])
        session.rollback()
