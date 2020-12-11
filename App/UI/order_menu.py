from Controllers.customer_controller import get_all_customers, simple_customer_find
from Controllers.car_controller import get_car_for_car_id, simple_car_find, simple_car_by_reg_num
from Controllers.employee_controller import get_all_employees
from Controllers.order_controller import make_new_order, get_uncompleted_orders, mark_order_as_completed, delete_order, get_all_orders


def order_menu():

    while True:
        print("Order Menu")
        print("==============")
        print("1. Make new Order")
        print("2. View all Orders that are not completed")
        print("3. Mark Order as Completed")
        print("4. View all Orders")
        print("5. Delete Order")
        print("6. Exit Order Menu")

        selection = input("> ")

        if selection == '1':  # make new order

            customers = get_all_customers()

            for customer in customers:
                print('-------------------')
                print(f' Customer Name: {customer.fullName} \n Customer ID: {customer._id}')

            cust_id = input("Enter Customer ID that you want to make an Order for: ")

            employees = get_all_employees()

            for employee in employees:
                print(employee)
                print('------------')

            empl_id = input("Enter Employee ID of the Employee who placed the order: ")

            one_customer = simple_customer_find(cust_id)
            if one_customer:
                for i in one_customer:
                    for j in i.regNumbers:
                        print('-------------------')
                        print("\n".join("{}\t{}".format(k, v) for k, v in j.items()))

            reg_num = input("Enter Registration number of the Car you want to make an order for: ")
            car_id = input("Enter Car ID of the Car you want to make an order for: ")

            #   car_id = simple_car_by_reg_num(reg_num)
            car = simple_car_find(car_id)
            if car:
                for i in car:
                    if i.parts:
                        for j in i.parts:
                            print('-------------------')
                            print("\n".join("{}\t{}".format(k, v) for k, v in j.items()))
                    else:
                        print('-------------------')
                        print('No parts found for that car')
                        print('-------------------')

            else:
                print("Could not find Car with id: ", cust_id)

            part_ids = []

            new_part_id = ''

            while new_part_id != 'quit':

                new_part_id = input("Enter Part ID of part that you want on Order, or enter 'quit': ")

                if new_part_id != 'quit':
                    part_ids.append(new_part_id)
                    print('Done!')
            make_new_order(cust_id, empl_id, reg_num, part_ids)

        elif selection == '2': # View all Orders that are not completed
            orders = get_uncompleted_orders()

            for order in orders:    # TODO Printa separat

                print(order)

        elif selection == '3': # Mark order as completed

            orders = get_uncompleted_orders()

            for order in orders:
                print('-------------------')
                print(f' Order ID: {order._id} \n Registration Number: {order.registrationNumber} \n')

            #for idx, order in enumerate(orders, start=1):
                #print('-------------------')
                #print(f'{idx}, \n Order ID: {order._id} \n Registration Number: {order.registrationNumber} \n')

            order_id = input('Enter Order ID of the order that you want to mark as completed: ')
            mark_order_as_completed(order_id)

        elif selection == '4':  # view all orders

            orders = get_all_orders()
            for order in orders:
                print('-------------------')
                print(f' Order ID: {order._id} \n Customer Number: {order.customerId} \n Employee ID: {order.employeeId}'
                      f' Registration Number of Customers car: {order.registrationNumber}')
                for IDs in order.partIds:
                    print(f' ID of Ordered part: {IDs}')
                print(f' Order date: {order.orderDate} \n Completed: {order.completed} \n Total Price: {order.sumPrice}')

        elif selection == '5': #     Delete order

            orders = get_all_orders()
            for order in orders:
                print('-------------------')
                print(
                    f' Order ID: {order._id} \n Customer Number: {order.customerId} \n Employee ID: {order.employeeId}'
                    f' Registration Number of Customers car: {order.registrationNumber}')
                for IDs in order.partIds:
                    print(f' ID of Ordered part: {IDs}')
                print(
                    f' Order date: {order.orderDate} \n Completed: {order.completed} \n Total Price: {order.sumPrice}')

            choice = input('Enter Order ID of order that is to be deleted: ')
            delete_order(choice)

        elif selection == '6':  # Exit menu
            break
