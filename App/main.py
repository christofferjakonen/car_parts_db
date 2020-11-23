from Data.db import Base, engine
from UI.main_menu import main_menu


def main():
    Base.metadata.create_all(engine)
    main_menu()


if __name__ == '__main__':
    main()
