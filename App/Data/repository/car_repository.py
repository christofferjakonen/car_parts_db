from Data.models.models import *
from bson import ObjectId
import re


def get_all_cars():

    cars = Car.all()
    return cars


def get_car_by_brand(brand):

    cars = Car.all()
    brand = brand.lower()
    matches = [cars[i] for i in range(len(cars)) if re.search(f'.*{brand}.*', str(cars[i].brand.lower()))]
    return matches


def get_car_for_car_id(car_id):

    cars = Car.all()
    matches = [cars[i] for i in range(len(cars)) if re.search(f'.*{car_id}.*', str(cars[i]._id))]

    return matches




def store_new_car(brand, model, color, model_year):


    new_car = Car({
        'brand': brand,
        'model': model,
        'color': color,
        'modelYear': model_year,
        'parts': []
    })
    new_car.save()
    print('Done!')


def delete_car(id):

    Car.delete(_id=ObjectId(id))
    print('done!')
    return None

"""
def view_parts_for_reg_num(reg):

    car = Car.find(_id=ObjectId(id)).first_or_none()

    return car.parts
"""


def add_part_to_car(car_id, part_id):

    car = Car.find(_id=ObjectId(car_id)).first_or_none()

    new_car = {
        "_id": car._id,
        "brand": car.brand,
        "model": car.model,
        "color": car.color,
        "modelYear": car.modelYear,
        "parts": car.parts
    }

    new_car['parts'].append({"part": ObjectId(part_id)})
    Car(new_car).save()

def simple_car_find(car_id):

    Car.find(_id=ObjectId(car_id)).first_or_none()

def simple_car_by_reg_num(reg_num):

    cars = get_all_cars()
    for thing in cars["regNumbers"]:
        if thing['regNumber'] == reg_num:
            return cars._id

