from Controllers.manufacture_controller import get_all_manufacturers, get_manufacturer_by_name, get_manufacturer_by_id,\
    add_new_manufacturer, update_manufacturer, delete_manufacturer_by_id

def manufacture_menu():
    while True:
        print("Manufacturers Menu")
        print("=========")
        print("1. Show All Manufacturers")
        print("2. Search for manufacturer")
        print("3. Add New Manufacturer")
        print("4. Update Manufacturer")
        print("5. Delete Manufacturer")
        print("6. Back")

        selection = input("> ")
        if selection == "1":
            # get everything
            print("\n=========")
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)
            print("=========")

        elif selection == "2":
            # search by full or partial id / name
            print("\n=========")
            choice = input("Get manufacturer 1. Id / 2. Manufacturer name / other. Exit\n> ")
            everything = get_all_manufacturers()
            for thing in everything:
                print(f"id: {thing._id}, Manufacturer: {thing.Manufacturer}")
            if choice == "1":
                searchId = input("Search by full or partial manufacturer id\n> ")
                manufacturers = get_manufacturer_by_id(searchId)
            elif choice == "2":
                searchName = input("Search by Full or partial manufacturer name\n> ")
                manufacturers = get_manufacturer_by_name(searchName)
            else:
                continue
            for manufacturer in manufacturers:
                print("=========")
                print(f"_id: {manufacturer._id}")
                print(f"Manufacturer: {manufacturer.Manufacturer}")
                print("Address: { ", end="")
                print(f"Country: {manufacturer.Address['Country']}, "
                      f"State: {manufacturer.Address['State']}, "
                      f"City: {manufacturer.Address['City']}, "
                      f"Zipcode: {manufacturer.Address['Zipcode']}, "
                      f"StreetAddress: {manufacturer.Address['StreetAddress']}, "
                      f"PhoneNumber: {manufacturer.Address['PhoneNumber']}", end="")
                print(" }")
                if manufacturer.Contacts:
                    print("Contacts: [")
                    for thing in manufacturer.Contacts:
                        print(f"Name: {thing['fullName']}, Phone number: {thing['phoneNumber']}, Email: {thing['email']}")
                    print("]")
                else:
                    print("Contacts: []")

        elif selection == "3":
            # add new
            print("\n=========")
            print("Add new manufacturer")

            name = input("Manufacturer name: ")
            if name:
                pass
            else:
                print("Manufacturer needs a name")
                continue
            country = input("Manufacturer country: ")
            state = input("(Optional) Manufacturer state: ")
            city = input("Manufacturer city: ")
            zipnum = input("Manufacturer zipcode: ")
            address = input("Manufacturer street address: ")
            phone = input("Manufacturer phone number: ")

            add_new_manufacturer(name, country, state, city, zipnum, address, phone)
            print("=========")

        elif selection == "4":
            # update
            print("\n=========")
            print("Update manufacturer by id")
            everything = get_all_manufacturers()
            for thing in everything:
                print(f"id: {thing._id}, Manufacturer: {thing.Manufacturer}")
            searchId = input("id: ")
            if searchId:
                pass
            else:
                continue
            search = get_manufacturer_by_id(searchId)[0]
            print(f"1. Manufacturer: {search.Manufacturer}")
            print("2. Address: { ", end="")
            print(f"Country: {search.Address['Country']}, "
                  f"State: {search.Address['State']}, "
                  f"City: {search.Address['City']}, "
                  f"Zipcode: {search.Address['Zipcode']}, "
                  f"StreetAddress: {search.Address['StreetAddress']}, "
                  f"PhoneNumber: {search.Address['PhoneNumber']}", end="")
            print(" }")
            if search.Contacts:
                print("3. Contacts: [")
                for thing in search.Contacts:
                    print(f"Name: {thing['fullName']}, Phone number: {thing['phoneNumber']}, Email: {thing['email']}")
                print("]")
            else:
                print("3. Contacts: []")

            columnNr = input("Column nr: ")
            if columnNr == "1":
                update_manufacturer(searchId, "1", input("New Value: "))
            elif columnNr == "2":
                new_address = search.Address
                print(f"1. Country: {search.Address['Country']}")
                print(f"2. State: {search.Address['State']}")
                print(f"3. City: {search.Address['City']}")
                print(f"4. Zipcode: {search.Address['Zipcode']}")
                print(f"5. StreetAddress: {search.Address['StreetAddress']}")
                print(f"6. PhoneNumber: {search.Address['PhoneNumber']}")
                columnNrJr = input("Column nr: ")
                newValue = input("New Value: ")
                if columnNrJr == "1":
                    new_address['Country'] = newValue
                if columnNrJr == "2":
                    new_address['State'] = newValue
                if columnNrJr == "3":
                    new_address['City'] = newValue
                if columnNrJr == "4":
                    new_address['Zipcode'] = newValue
                if columnNrJr == "5":
                    new_address['StreetAddress'] = newValue
                if columnNrJr == "6":
                    new_address['PhoneNumber'] = newValue
                update_manufacturer(searchId, "2", new_address)
            elif columnNr == "3":
                while True:
                    choice = input("1. Add new contact / 2. Edit existing contact / other. Exit\n> ")
                    if choice == "1":
                        # new contact
                        name = input("Full name: ")
                        phone = input("Phone number: ")
                        email = input("Email: ")
                        newValue = {
                            "fullName": name,
                            "phoneNumber": phone,
                            "email": email
                        }
                        update_manufacturer(searchId, "3", newValue)

                    elif choice == "2":
                        # existing contact
                        # -----------------
                        for i, contact in enumerate(search.Contacts, start=1):
                            print(f"{i}. Full name: {contact['fullName']}, Phone number: {contact['phoneNumber']}, Email: {contact['email']}")
                        index = input("Choose contact to edit\n> ")
                        # -----------------
                        if index and index.isnumeric() and 0 <= int(index)-1 < len(search.Contacts):
                            index = int(index)-1
                        else:
                            print("Invalid contact")
                            break
                        # -----------------
                        while True:
                            print(f"1. Full name: {search.Contacts[index]['fullName']}")
                            print(f"2. Phone number: {search.Contacts[index]['phoneNumber']}")
                            print(f"3. Email: {search.Contacts[index]['email']}")
                            print("other. Exit")
                            choice = input("What to edit\n> ")
                            if choice not in ["1", "2", "3"]:
                                break
                            newValue = input("New value\n> ")
                            updated_contact = search.Contacts[index]
                            if choice == "1":
                                updated_contact['fullName'] = newValue
                            elif choice == "2":
                                updated_contact['phoneNumber'] = newValue
                            elif choice == "3":
                                updated_contact["email"] = newValue
                            update_manufacturer(searchId, "4", updated_contact, index)
                    else:
                        break
            else:
                print("Invalid column")
                continue
            # newValue = input("New Value: ")
            #
            # update_manufacturer(searchId, columnNr, newValue)

        elif selection == "5":
            print("\n=========")
            print("Delete manufacturer by id")
            everything = get_all_manufacturers()
            for thing in everything:
                print(f"id: {thing._id}, Manufacturer: {thing.Manufacturer}")
            searchId = input("id: ")
            if searchId:
                delete_manufacturer_by_id(searchId)

        elif selection == "6":
            break

        else:
            continue
