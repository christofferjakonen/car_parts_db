from Controllers.parts_controller import get_all_parts, get_part_by_id, \
    delete_part_by_id, update_part_by_id, get_part_by_name, add_new_part, get_part_by_product_number

def parts_menu():
    while True:
        print("\nParts Menu")
        print("=========")
        print("1. Show All Parts")
        print("2. Search for part")
        print("3. Add new part")
        print("4. Edit part by id")
        print("5. Delete part by id")
        print("6. Exit")

        selection = input("> ")

        if selection == "1":
            # get everything
            print("\n=========")
            parts = get_all_parts()
            for part in parts:
                print(part)
                print("=========")

        elif selection == "2":
            print("\n=========")
            choice = input("Get part by 1: id / 2: name / 3: product number / other: exit\n> ")
            everything = get_all_parts()
            for thing in everything:
                print(f"id: {thing._id}, Product name: {thing.Product_Name}, Product number: {thing.Product_Number}")

            if choice == "1":
                searchID = input("Enter full or partial id: ")
                parts = get_part_by_id(searchID)
            elif choice == "2":
                partName = input("Enter full or partial product name: ")
                parts = get_part_by_name(partName)
            elif choice == "3":
                partNumber = input("Enter full or partial product number: ")
                parts = get_part_by_product_number(partNumber)
            else:
                continue
            print("=========")
            for part in parts:
                print(part)
                print("=========")

        elif selection == "3":
            # add new part
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
            add_new_part(partId, partName, manufacturer, partDescription, purchasePrice, sellPrice)

        elif selection == "4":
            # edit part
            # choose product by id and edit value in a column
            print("\n=========")
            everything = get_all_parts()
            for thing in everything:
                print(f"id: {thing._id}, Product name: {thing.Product_Name}, Product number: {thing.Product_Number}")
            partID = input("id: ")
            if partID:
                pass
            else:
                continue
            search = get_part_by_id(partID)[0]
            print(f"1. Product number: {search.Product_Number}")
            print(f"2. Product name: {search.Product_Name}")
            print(f"3. Manufacturer: {search.Manufacturer}")
            print(f"4. Product description: {search.Product_Description}")
            print(f"5. Buy price: {search.Buy_Price}")
            print(f"6. Sell price: {search.Sell_Price}")
            columnNr = input("Column nr: ")
            if columnNr and columnNr.isnumeric() and 1 <= int(columnNr) <= 6:
                columnNr = int(columnNr)
            else:
                print("Invalid column")
                continue
            newValue = input("New Value: ")

            update_part_by_id(partID, columnNr, newValue)

        elif selection == "5":
            # delete part
            print("\n=========")
            everything = get_all_parts()
            for thing in everything:
                print(f"id: {thing._id}, Product name: {thing.Product_Name}, Product number: {thing.Product_Number}")
            command = input("ID of part to delete: ")
            if command:
                delete_part_by_id(command)

        elif selection == "6":
            break

        elif selection == "7":
            # add / edit storage location to part
            print("\n=========")
            print("Add / Edit storage location of part:")
            # show all parts
            everything = get_all_parts()
            for thing in everything:
                print(f"id: {thing._id}, Product name: {thing.Product_Name}, Product number: {thing.Product_Number}")
            # select part
            partID = input("id: ")
            if partID:
                pass
            else:
                continue
            search = get_part_by_id(partID)[0]
            # list existing storage spots, numbered for selection
            print(f"Storage space(s) for part: {search.Product_Name}\n")
            if search.Warehouse:
                for i, place in enumerate(search.Warehouse, start=1):
                    print(f"{i}. {place}")
            else:
                print("No storage locations found\n")
            while True:
                # choose to add a new storage spot or to change an existing one
                choice = input("1: Add new storage location\n2: Edit existing storage location\n3: Break\n> ")
                if choice == "1":
                    while True:
                        print("New storage location:\n")
                        aisle = input("Aisle: ")
                        bay = input("Bay: ")
                        shelf = input("Shelf: ")
                        for i in range(len(search.Warehouse)):
                            if search.Warehouse[i]["Aisle"] == aisle and search.Warehouse[i]["Bay"] == bay and search.Warehouse[i]["Shelf"] == shelf:
                                print("Location is already occupied")
                                continue
                            else:
                                pass
                        amount = input("Amount in stock: ")
                        auto_limit = input("(Optional) Amount at which to automatically buy more: ")
                        if not auto_limit:
                            auto_limit = None
                        auto_amount = input("(Optional) Amount to automatically buy: ")
                        if not auto_amount:
                            auto_amount = None
                        expected_date = "None"
                        # todo expected delivery date is updated on auto buy and set to current time of the order + a delta from the supplier?
                        break
                    newValue = {
                        "Aisle": aisle,
                        "Bay": bay,
                        "Shelf": shelf,
                        "AmountInStock": amount,
                        "AutoBuyLimit": auto_limit,
                        "AutoBuyAmount": auto_amount,
                        "ExpectedDeliveryDate": expected_date
                    }
                    update_part_by_id(search._id, 8, newValue)

                elif choice == "2":
                    if search.Warehouse:
                        location_nr = input("Which location to edit?\n> ")
                        if location_nr and location_nr.isnumeric() and 0 <= int(location_nr)-1 < len(search.Warehouse):
                            location_nr = int(location_nr)-1
                        else:
                            continue
                        while True:
                            wh_temp = search.Warehouse[location_nr]
                            print(f"1. Aisle: {wh_temp['Aisle']}")
                            print(f"2. Bay: {wh_temp['Bay']}")
                            print(f"3. Shelf: {wh_temp['Shelf']}")
                            print(f"4. Amount in stock: {wh_temp['AmountInStock']}")
                            print(f"5. Auto buy limit: {wh_temp['AutoBuyLimit']}")
                            print(f"6. Auto buy amount: {wh_temp['AutoBuyAmount']}")
                            print(f"7. Expected delivery date: {wh_temp['ExpectedDeliveryDate']}")
                            print("other. Exit")
                            choice = input("Line to edit: ")
                            if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                                break
                            newValue = input("New value\n> ")
                            if choice == "1":
                                wh_temp['Aisle'] = newValue
                            elif choice == "2":
                                wh_temp['Bay'] = newValue
                            elif choice == "3":
                                wh_temp["Shelf"] = newValue
                            elif choice == "4":
                                wh_temp["AmountInStock"] = newValue
                            elif choice == "5":
                                wh_temp["AutoBuyLimit"] = newValue
                            elif choice == "6":
                                wh_temp["AutoBuyAmount"] = newValue
                            elif choice == "7":
                                wh_temp["ExpectedDeliveryDate"] = newValue
                            update_part_by_id(partID, 8, wh_temp, location_nr)

                        # change:
                        # select which storage spot to edit
                    else:
                        print("No storage location to edit\n")
                        continue
                else:
                    continue
                break

        else:
            continue
