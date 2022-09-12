#!/usr/bin/python3
"""module, selects * from states table in hbtn_0e_0_usa
database filters out nonstartswith N"""


import MySQLdb
import sys


def main():
    """ main function """
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db, charset="utf8")
    cur = conn.cursor()
    query = "select * from states where states.name like 'n%'\
             or states.name like 'N%' order by states.id"
    cur.execute(query)
    res = cur.fetchall()
    for item in res:
        print(item)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
