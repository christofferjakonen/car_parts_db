from UI.parts_menu import parts_menu


def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Parts")
        print("2. Exit")

        selection = input("> ")
        if selection == "1":
            parts_menu()

        if selection == "2":
            break


if __name__ == '__main__':
    main_menu()