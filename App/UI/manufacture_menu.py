from Controllers.manufacture_controller import get_all_manufacturers

def manufacture_menu():
    while True:
        print("Manufacturers Menu")
        print("=========")
        print("1. Show All Manufacturers")

        selection = input("> ")
        if selection == "1":
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)

        else:
            break