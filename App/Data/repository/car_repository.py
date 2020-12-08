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

def get_reg_number_for_car(id):

    cars = Car.all()

    matches = [cars[i] for i in range(len(cars)) if re.search(f'.*{id}.*', str(cars[i].regNumbers))]
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


def view_parts_for_reg_num(reg):

    car = Car.find(_id=ObjectId(id)).first_or_none()

    return car.parts

def get_car_for_car_id(car_id):

    cars = Car.all()
    matches = [cars[i] for i in range(len(cars)) if re.search(f'.*{car_id}.*', str(cars[i]._id))]

    return matches

