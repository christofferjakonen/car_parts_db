from Controllers.manufacture_controller import get_all_manufacturers, add_new_manufacturer, update_manufacturer

def manufacture_menu():
    while True:
        print("Manufacturers Menu")
        print("=========")
        print("1. Show All Manufacturers")
        print("4. Add New Manufacturer")
        print("5. Update Manufacturer")

        selection = input("> ")
        if selection == "1":
            # get everything
            print("\n=========")
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)
            print("=========")

        elif selection == "4":
            # add new
            print("\n=========")
            print("Add new manufacturer")

            name = input("Manufacturer name: ")
            if name:
                pass
            else:
                print("Manufacturer needs a name")
                continue

            add_new_manufacturer(name, country, state, city, zipnum, address, phone)
            print("=========")

        elif selection == "5":
            # update
            pass

        else:
            break