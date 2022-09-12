#!/usr/bin/python3
""" module contains sql query using dbapi"""


import MySQLdb
import sys


def main():
    """program entry"""
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(passwd=pwd, db=db, user=usr)
    # conn = MySQLdb.connect(host="localhost", port=3306,
    #                       user=usr, passwd=pwd,
    #                       db=db, charset="utf8")
    cur = conn.cursor()
    query = "select cities.name from\
            cities join states on cities.state_id = states.id\
            where states.name = %s\
            order by cities.id"
    cur.execute(query, (state,))
    res = cur.fetchall()
    for i in res:
        if i is not res[0]:
            print(", ", end='')
        print(i[0], end='')
    print()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
