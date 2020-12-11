from Data.models.models import *
from bson import ObjectId
import re


def get_all_customers():


    return Customer.all()



def simple_customer_find(id):
    return Customer.find(_id=ObjectId(id))

def get_customer_by_id(car_id):

    customers = Customer.all()
    matches = [customers[i] for i in range(len(customers)) if re.search(f'.*{car_id}.*', str(customers[i]._id))]
    return matches
    #return Customer.find(_id=ObjectId(id))


def get_customer_by_name(pattern):

    customers = Customer.all()
    pattern = pattern.lower()
    matches = [customers[i] for i in range(len(customers)) if re.search(f'.*{pattern}.*', customers[i].name.lower())]
    return matches


def store_new_customer(name, phone_number, email, contact_person=None):

    new_customer = Customer({
        "fullName": name,
        "phoneNumber": phone_number,
        "email": email,
        "regNumbers": [],
        "contactPerson": []
        })
    if contact_person:
        new_customer["contactPerson"] = contact_person
    new_customer.save()


def delete_customer(id):


    Customer.delete(_id=ObjectId(id))
    print('done!')
    return None


def add_car_to_customer(cust_id, reg_num, car_id):

    customer = Customer.find(_id=ObjectId(cust_id)).first_or_none()

    new_customer = {
        "_id": customer._id,
        "fullName": customer.fullName,
        "phoneNumber": customer.phoneNumber,
        "email": customer.email,
        "regNumbers": customer.regNumbers,
        "contactPerson": customer.contactPerson
    }

    new_customer['regNumbers'].append({"regNumber": reg_num, "carId": ObjectId(car_id)})
    Customer(new_customer).save()

    print('Done!')


def delete_reg_num(cust_num, reg_num):

    customer = Customer.find(_id=ObjectId(cust_num)).first_or_none()


    new_customer = {
        "_id": customer._id,
        "fullName": customer.fullName,
        "phoneNumber": customer.phoneNumber,
        "email": customer.email,
        "regNumbers": customer.regNumbers,
        "contactPerson": customer.contactPerson
    }

    new_customer['regNumbers'] = [x for x in new_customer if reg_num not in x]
    Customer(new_customer).save()

    print('Done!')



def get_reg_number_for_customer(id):

    reg_num = session.query(RegNumber.RegNumber).filter(RegNumber.CustomerID == id).all()

    car_id = session.query(RegNumber.CarID).filter(RegNumber.CustomerID == id).all()

    return reg_num, car_id
