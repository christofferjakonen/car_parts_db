from UI.customers_menu import customers_menu
from UI.car_menu import car_menu


def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Customers")
        print("2. Cars")
        print("3. -")
        print("4. Quit")

        selection = input("> ")
        if selection == "1":
            customers_menu()

        elif selection == "2":
            car_menu()

        elif selection == '4':
            break



def main():

    main_menu()



if __name__ == "__main__":
    main()

