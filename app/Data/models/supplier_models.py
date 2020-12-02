from .document_model import Document
from Data.db import mdb


class Supplier(Document):
    collection = mdb.suppliers


class SupplierContactPerson(Document):
    collection = mdb.supplier_contact_persons


class SupplierAddress(Document):
    collection = mdb.supplier_addresses


class SupplierHasPart(Document):
    collection = mdb.supplier_has_parts


class SupplierHasManufacturer(Document):
    collection = mdb.suppliers_have_manufacturer
