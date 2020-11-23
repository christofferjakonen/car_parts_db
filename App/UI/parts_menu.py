from Controllers.parts_controller import get_all_parts

def parts_menu():
    while True:
        print("Parts Menu")
        print("=========")
        print("1. Show All Parts")
        print("2. Exit")

        selection = input("> ")
        if selection == "1":
            print("\n=========")
            parts = get_all_parts()
            for part in parts:
                print(part)
            print("=========\n")

        if selection == "2":
            break
