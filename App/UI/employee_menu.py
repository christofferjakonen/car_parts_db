from Controllers.employee_controller import get_all_employees, get_employee_by_name, \
    get_employee_by_id, add_new_employee, update_employee
from Controllers.store_controller import get_all_stores

def employee_menu():
    while True:
        print("\nEmployee Menu")
        print("=========")
        print("1. Get all employees")
        print("2. Search for employee")
        print("3. Add new employee")
        print("4. Edit employee")
        print("9. Back")

        selection = input("> ")

        if selection == "1":
            # get everything
            print("\n=========")
            employees = get_all_employees()
            for employee in employees:
                print(employee)
            print("=========")

        elif selection == "2":
            # get by search
            # search by full or partial id / name
            print("\n=========")
            choice = input("Get employee by 1. Id / 2. Name / other. Exit\n> ")
            everything = get_all_employees()
            for thing in everything:
                print(f"id: {thing._id}, Employee name: {thing.Full_Name}")
            if choice == "1":
                searchId = input("Search by full or partial employee id\n> ")
                employees = get_employee_by_id(searchId)
            elif choice == "2":
                searchName = input("Search by Full or partial employee name\n> ")
                employees = get_employee_by_name(searchName)
            else:
                continue
            for employee in employees:
                print("=========")
                print(f"_id: {employee._id}")
                print(f"Employee name: {employee.Full_Name}")
                print(f"Working in store: {employee.Store}")
                print("Address:")
                for key, value in employee.Address.items():
                    print(f"\t{key}: {value}")
                print(f"Pay: {employee.Pay}/hour")

        elif selection == "3":
            # add new
            print("\n=========")
            print("Add new employee")
            everything = get_all_stores()
            for thing in everything:
                print(f"id: {thing._id}, Address: {thing.Address}")
            store = input("id of store to add employee to: ")
            name = input("Employee name: ")
            if name:
                pass
            else:
                print("Employee needs a name")
                continue
            phone = input("Employee phone number: ")
            pay = input("Employee pay/hour: ")
            country = input("Employee mail country: ")
            state = input("(Optional) Employee mail state: ")
            if not state:
                state = "None"
            city = input("Employee mail city: ")
            zipnum = input("Employee mail zipcode: ")
            address = input("Employee mail street address: ")

            add_new_employee(name, country, state, city, zipnum, address, phone, store, pay)
            print("=========")

            # edit existing
            # delete

        elif selection == "4":
            # edit existing employee
            print("\n=========")
            print("Update Employee by id")
            everything = get_all_employees()
            for thing in everything:
                print(f"id: {thing._id}, Employee name: {thing.Full_Name}")
            searchId = input("id: ")
            if searchId:
                pass
            else:
                continue
            search = get_employee_by_id(searchId)[0]
            print(f"1. Employee name: {search.Full_Name}")
            print(f"2. Working in store: {search.Store}")
            print(f"3. Address: {{ "
                  f"Country: {search.Address['Country']}, "
                  f"State: {search.Address['State']}, "
                  f"City: {search.Address['City']}, "
                  f"Zipcode: {search.Address['Zipcode']}, "
                  f"StreetAddress: {search.Address['StreetAddress']}, "
                  f"PhoneNumber: {search.Address['PhoneNumber']}", end=" }\n")
            print(f"4. Pay: {search.Pay}")
            columnNr = input("Column nr: ")

            if columnNr == "1":
                update_employee(searchId, "1", input("New Value: "))

            elif columnNr == "2":
                everything = get_all_stores()
                for thing in everything:
                    print(f"id: {thing._id}, Address: {thing.Address}")
                store = input("New Value: ")
                update_employee(searchId, "2", store)

            elif columnNr == "3":
                while True:
                    for i, key, value in enumerate(search.Address.items(), start=1):
                        print(f"{i}. {key}: {value}")
                    index = input("Column nr / other to exit: ")
                    if index and index.isnumeric() and 0 <= int(index) - 1 < len(search.Address):
                        index = int(index) - 1
                    else:
                        break
                    newValue = input("New Value: ")
                    update_employee(searchId, "3", newValue, index)

            elif columnNr == "4":
                update_employee(searchId, "4", input("New pay/hour: "))

            else:
                print("Invalid column")
                continue

        elif selection == "5":
            # delete employee
            pass

        elif selection == "9":
            break

        else:
            continue
