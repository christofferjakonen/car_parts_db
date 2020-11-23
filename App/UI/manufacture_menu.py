from Controllers.manufacture_controller import get_all_manufacturers

def parts_menu():
    while True:
        print("Parts Menu")
        print("=========")
        print("1. Show All Parts")

        selection = input("> ")
        if selection == "1":
            parts = get_all_manufacturers()
            for part in parts:
                print(part)

        else:
            break