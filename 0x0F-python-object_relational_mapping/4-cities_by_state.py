#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    query = """SELECT cities.id, cities.name, states.name
                FROM cities
                   INNER JOIN states
                  ON cities.state_id = states.id
                ORDER BY cities.id;"""

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)


if __name__ == "__main__":
    main()
