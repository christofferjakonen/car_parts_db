from Controllers.customers_controller import get_all_reg_numbers, get_all_customers, get_customer_by_id, get_customer_by_name, store_changes, \
    store_new_customer, delete_customer, change_name, add_car_to_customer, delete_reg_num, get_reg_number_for_customer
from Controllers.car_controller import get_car_by_id

def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("1. View All Customers")
        print("2. View Customer by Id")
        print("3. Find Customers by Name")
        print("4. View All Registration numbers")
        print("5. Add new Customer")
        print("6. Delete Customer")
        print("7. Change Customer Name")
        print("8. Add Car to Customer")
        print("9. Remove Car from Customer")
        print("10. View Registration number and CarID for CustomerID")
        print("11. Quit Customers Menu")

        selection = input("> ")

        if selection == "1":
            customers = get_all_customers()
            for customer in customers:
                print(customer)

        elif selection == "2":
            id = input("Enter Customer Id: ")
            customer = get_customer_by_id(id)
            if customer:
                print(customer)
            else:
                print("Could not find customer with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial customer name: ")
            customers = get_customer_by_name(pattern)
            for key, customer in customers.items():
                print(f'{key}. {customer}')

        elif selection == "4":
            reg_numbers = get_all_reg_numbers()

            for reg_num in reg_numbers:
                print(reg_num)




        elif selection == "5":

            new_name = input("Enter new Name: ")
            store_new_customer(new_name)


        elif selection == "6":

            id = int(input("Enter Customer Id to be removed: "))
            delete_customer(id)


        elif selection == "7":

            old_name = str(input("Enter Customer´s name that you want to change: "))
            name = str(input("Enter the new name: "))
            change_name(old_name, name)

        elif selection == "8":

            cust_id = int(input("Enter Customer ID that you want to assign a car to: "))
            car_id = int(input("Enter Car ID of the car that you want to the Customer"))
            reg_num = str(input("Enter Registration Number of the Car with that ID number"))
            add_car_to_customer(cust_id, reg_num, car_id)

        elif selection == "9":
            reg_num = str(input("Enter Registration number of the Car to be removed: "))
            delete_reg_num(reg_num)

        elif selection == "10":
            id = input("Enter Customer Id: ")
            reg_number = get_reg_number_for_customer(id)

            for i in range(len(reg_number[0])):
                print(f"Registration number: {reg_number[0][i][0]}, CarID: {reg_number[1][i][0]}\n")

        elif selection == "11":
            break


