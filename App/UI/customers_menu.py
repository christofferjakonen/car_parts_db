from Controllers.customers_controller import get_all_reg_numbers, get_all_customers, get_customer_by_id, get_customer_by_name, store_changes, \
    store_new_first_name


def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("1. View All Customers")
        print("2. View Customer by Id")
        print("3. Find Customers by Name")
        print("4. View All Registration numbers")
        print("5. Edit a Customer")
        print("6. Quit Customers Menu")

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
            for reg_number in reg_numbers:
                print(reg_number)

        elif selection == "5":

            customer = get_all_customers()
            for customers in customer:
                print(customers)
            edit_selection = input("Enter number for customer to edit: ")
            edit_selection = int(edit_selection)

            customer = customers[edit_selection]
            print(f'1. Customer Name: {customer.CustomerName}')
            print(f'2. Customer ID: {customer.CustomerID}')

            line = input("Enter number for what line to edit: ")

            if line == "2":
                new_value = input("Enter new Name: ")
                store_new_first_name(customer, new_value)
        else:
            break
