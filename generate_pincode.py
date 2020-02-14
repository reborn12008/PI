from random import randrange
import sqlite3
from sqlite3 import Error


def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e)

    return conn


def update_task(c):
    cur = c.cursor()
    number_of_regists = cur.execute("SELECT * FROM source_acesso;")
    for i in number_of_regists.fetchall():
        pin = randrange(9999)
        cur.execute("UPDATE source_acesso SET pincode=" + str(pin) + " WHERE id=" + str(i[0]) + ";")
    c.commit()


def main():
    database = r"db.sqlite3"
    conn = create_connection(database)
    with conn:
        update_task(conn)


if __name__ == '__main__':
    main()
