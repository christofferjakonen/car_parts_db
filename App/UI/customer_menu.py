from Controllers.customer_controller import store_new_customer, get_all_customers, get_customer_by_id, get_customer_by_name, \
     delete_customer, add_car_to_customer, delete_reg_num, get_reg_number_for_customer
from Controllers.car_controller import get_all_cars


def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("1. View All Customers")
        print("2. View Customer by Id")
        print("3. Find Customers by Name")
        print("4. Add new Customer")
        print("5. Add Car to Customer")
        print("6. Remove Car from Customer")
        print('7. Delete customer')
        print("8. Quit Customers Menu")

        selection = input("> ")

        if selection == "1":    # View all customers
            customers = get_all_customers()
            for customer in customers:
                print(customer.fullName)
                print('-----------------')

        elif selection == "2":  # View customer by ID

            customers = get_all_customers()
            for customer in customers:
                print(customer.fullName, customer._id)
                print('-----------------')

            cust_id = input("Enter Customer Id: ")
            one_customer = get_customer_by_id(cust_id)
            if one_customer:
                for i in one_customer:
                    print(i)
            else:
                print("Could not find customer with id ", cust_id)

        elif selection == "3":  # Find customers by name


            while True:

                pattern = input("Enter part of customer name: ")

                if pattern:
                    customers = get_customer_by_name(pattern)
                    for customer in customers:
                        print(customer)
                        print('-------------')

                    break

                else:
                    continue

        elif selection == "4":  # Store new customer

            name = input("Enter new Personal or Company Name: ")
            contact_person = input("Enter Name of Contact person for Company (Optional): ")
            phone_number = input('Enter phone number: ')
            email = input('Enter email: ')

            store_new_customer(name, phone_number, email, contact_person)

        elif selection == "5":      # Add car to customer

            customers = get_all_customers()
            for customer in customers:
                print(customer)
                print('-----------------')

            cust_id = input("Enter Customer ID that you want to assign a car to: ")

            cars = get_all_cars()
            for car in cars:
                print(car)
                print('-----------------')
            car_id = input("Enter Car ID of the car that you want to assign to the Customer")
            reg_num = input("Enter Registration Number of the Car")

            add_car_to_customer(cust_id, reg_num, car_id)

        elif selection == "6":  # Remove Car from Customer
            customers = get_all_customers()
            for customer in customers:
                print(f' Customer ID: {customer._id} Name: {customer.fullName} Registration number(s): {customer.regNumbers}')
                print('-----------------')

            cust_nr = input("Enter Customer number of customer who´s Registration number is to be Removed")

            reg_nr = input("Enter Registration number of the Car to be removed: ")
            delete_reg_num(cust_nr, reg_nr)


        elif selection == "7":  #Delete customer
            customers = get_all_customers()
            for customer in customers:
                print(customer)
                print('-----------------')
            id = (input("Enter Customer Id to be removed: "))
            delete_customer(id)

        elif selection == "8":
            break


