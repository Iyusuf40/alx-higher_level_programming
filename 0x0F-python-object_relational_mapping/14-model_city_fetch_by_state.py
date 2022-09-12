#!/usr/bin/python3
""" sqlalchemy join"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import State


def main():
    """main function"""
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    db_url = f"mysql+mysqldb://{user}:{pwd}@localhost/{db}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        string_sub = f"{city.state.name}: ({city.id}) {city.name}"
        print(string_sub)


if __name__ == "__main__":
    main()
