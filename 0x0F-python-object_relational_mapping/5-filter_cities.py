#!/usr/bin/python3
"""
lists all cities of a state passed as argumentfrom the database
hbtn_0e_0_usa in ascending order by cities.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    state_searched = sys.argv[4]
    c = db.cursor()
    c.execute("""SELECT cities.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC""", (state_searched,))
    print(", ".join([city[0] for city in c.fetchall()]))
    c.close()
    db.close()
