#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    my_cursor = my_db.cursor()
    my_cursor.execute("""SELECT * FROM cities
                        INNER JOIN states
                        ON cities.state_id = states.id
                        ORDER BY cities.id""")
    print(", ".join([city[2]
                    for city in my_cursor.fetchall()
                    if city[4] == argv[4]]))
    my_cursor.close()
    my_db.close()
