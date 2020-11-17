from db import Base, engine, session
from models.manufacture import Manufacture
from models.part import Part


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
