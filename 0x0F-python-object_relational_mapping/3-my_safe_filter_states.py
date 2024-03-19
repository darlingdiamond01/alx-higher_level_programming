#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    my_cursor = my_db.cursor()
    my_cursor.execute("""SELECT * FROM states WHERE name=%s
                        ORDER BY id""", (argv[4],))
    my_data = my_cursor.fetchall()
    for row in my_data:
        print(row)
    my_cursor.close()
    my_db.close()
