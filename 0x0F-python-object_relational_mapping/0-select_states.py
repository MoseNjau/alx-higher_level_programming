#!/usr/bin/python3
"""
lists all states from the database
hbtn_0e_0_usa in ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM `states` ORDER BY id ASC""")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
