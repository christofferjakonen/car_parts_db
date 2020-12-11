from Data.models.models import *
from bson import ObjectId
import re


def get_all_employees():

    return Employee.all()