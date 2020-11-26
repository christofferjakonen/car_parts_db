from Controllers.parts_controller import get_all_parts, get_part_by_id, \
    delete_part_by_ID, update_part_by_ID, get_part_by_name, add_new_part

def parts_menu():
    while True:
        print("Parts Menu")
        print("=========")
        print("1. Show All Parts")
        print("2. Search part by id")
        print("3. Search part by name")
        print("4. Add new part")
        print("5. Edit part by id")
        print("6. Delete part by id")
        print("7. Exit")

        selection = input("> ")

        if selection == "1":
            # get everything
            print("\n=========")
            parts = get_all_parts()
            for part in parts:
                print(part)
            print("=========")

        elif selection == "2":
            # search by id
            print("\n=========")
            searchID = int(input("ID: "))
            print(get_part_by_id(searchID))
            print("=========")

        elif selection == "3":
            # search by name
            partName = input("Enter full or partial part name: ")
            parts = get_part_by_name(partName)
            for key, part in parts.items():
                print(f'{key}. {part}')

        elif selection == "4":
            # add new part
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
            add_new_part(partId, partName, manufacturer, partDescription, purchasePrice, sellPrice)

        elif selection == "5":
            # edit part
            print("\n=========")
            partID = int(input("ID: "))
            part = get_part_by_id(partID)
            print(f"1. Part Name: {part.ProductName}")
            print(f"2. Part ID: {part.ProductNum}")
            print(f"3. Part Description: {part.PartDescription}")
            print(f"4. Part Manufacturer: {part.Manufacture}")
            print(f"5. Part Cost: {part.PurchasePrice}")
            print(f"6. Part Sell price: {part.SellPrice}")
            print("=========")

            columnNr = int(input("Column Nr to edit: "))
            update_part_by_ID(partID, columnNr)


        elif selection == "6":
            # delete part
            print("\n=========")
            command = int(input("ID of part to delete: "))
            if command:
                delete_part_by_ID(command)

        elif selection == "7":
            break

        else:
            continue
