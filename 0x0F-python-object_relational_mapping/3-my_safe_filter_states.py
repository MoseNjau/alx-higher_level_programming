#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    query = "SELECT * FROM states"

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        if state[1] == state_name:
            print(state)


if __name__ == "__main__":
    main()
