#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” from
the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    my_session_maker = sessionmaker(bind=engine)
    my_session = my_session_maker()
    my_session.add(City(name="San Francisco", state=State(name="California")))
    my_session.commit()
    my_session.close()
