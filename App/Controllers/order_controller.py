import Data.repository.order_repository as orr


def get_all_orders():
    return orr.get_all_orders()


def make_new_order(cust_id, empl_id, reg_num, part_ids, store_id):
    return orr.make_new_order(cust_id, empl_id, reg_num, part_ids, store_id)


def get_uncompleted_orders():
    return orr.get_uncompleted_orders()


def mark_order_as_completed(order_id):
    return orr.mark_order_as_completed(order_id)


def delete_order(choice):
    return orr.delete_order(choice)
