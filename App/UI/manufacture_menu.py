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
            print("Add new part")

            partId = input("Part Id: ")
            if partId and partId.isnumeric():
                pass
            else:
                print("New part needs Id")
                continue
            partName = input("Part name: ")
            manufacturer = input("Parts manufacturer: ")
            partDescription = input("Part description: ")
            purchasePrice = input("Purchase price: ")
            sellPrice = input("Sell price: ")
            add_new_manufacturer
            print("=========")

        elif selection == "5":
            # update
            pass

        else:
            break