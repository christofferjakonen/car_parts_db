import datetime
from Data.models.models import *
from bson import ObjectId
import re


def get_all_orders():

    orders = Order.all()
    return orders


def make_new_order(cust_id, empl_id, reg_num, part_ids, store_id):

    prices_for_parts = []

    for part_id in part_ids:
        parts = Part.find(_id=ObjectId(part_id)).first_or_none()
        prices_for_parts.append(parts.Sell_Price)

    sum_price = 0

    for x in prices_for_parts:

        sum_price += float(re.sub(r"[^0-9.]", "", x))   # TODO Gör dict av part_id med value = antal delar
    sum_price = str(sum_price)
    currency = " kr"
    sum_price = (sum_price + currency)

    new_order = Order({
        'customerId': cust_id,
        'employeeId': empl_id,
        'registrationNumber': reg_num,
        'partIds': part_ids,
        'orderDate': datetime.datetime.now(),
        'completed': "No",
        'sumPrice': sum_price,
        'storeId': store_id
    })

    new_order.save()

    print('Done!')


def get_uncompleted_orders():

    orders = Order.find(**{'completed': 'No'})

    return orders


def mark_order_as_completed(order_id):

    order = Order.find(_id=ObjectId(order_id)).first_or_none()

    new_order = Order({
        'orderId': order._id,
        'customerId': order.customerId,
        'employeeId': order.employeeId,
        'registrationNumber': order.registrationNumber,
        'partIds': order.partIds,
        'orderDate': order.orderDate,
        'completed': datetime.datetime.now(),
        'sumPrice': order.sumPrice
    })
    print(new_order)
    new_order.save()
    print('Done!')


def delete_order(choice):

    Order.delete(_id=ObjectId(choice))
    print('Done!')



