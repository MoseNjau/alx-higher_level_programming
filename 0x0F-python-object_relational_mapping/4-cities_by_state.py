#!/usr/bin/python3
"""
lists all cities from the database
hbtn_0e_0_usa in ascending order by cities.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]
    c.close()
    db.close()
