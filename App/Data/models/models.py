from .document_model import Document
from Data.db import mdb


class Customer(Document):
    collection = mdb.customers


class Car(Document):
    collection = mdb.cars


class Order(Document):
    collection = mdb.orders


class Employee(Document):
    collection = mdb.employees


class Store(Document):
    collection = mdb.stores


class Part(Document):
    collection = mdb.parts

