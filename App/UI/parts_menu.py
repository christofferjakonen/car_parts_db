from Controllers.parts_controller import get_all_parts, get_part_by_id

def parts_menu():
    while True:
        print("Parts Menu")
        print("=========")
        print("1. Show All Parts")
        print("2. Show part by id")
        print("3. Edit part by id")
        print("4. Exit")

        selection = input("> ")
        if selection == "1":
            print("\n=========")
            parts = get_all_parts()
            for part in parts:
                print(part)
            print("=========\n")

        if selection == "2":
            print("\n=========")
            print(get_part_by_id(input("> ")))
            print("=========\n")

        if selection == "3":
            break
