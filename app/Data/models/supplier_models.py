from .document_model import Document
from Data.db import mdb


class Supplier(Document):
    collection = mdb.suppliers
