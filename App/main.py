from Date.db import Base, engine, session
from Data.models.manufacture import Manufacture
from Data.models.part import Part


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
