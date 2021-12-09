from pathlib import Path

import sqlite3




def sqlite_connection_factory():
    path = Path.home().joinpath('.sfl_assignment', 'users.db')
    conn = sqlite3.connect(str(path))
    return conn


def build_users_db(connection_factory):
    conn = connection_factory()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE users (
                   id integer,
                   first_name text,
                   last_name text,
                   email text,
                   gender text,
                   ip_address text

    )""")
    # cur.execute("""INSERT INTO users VALUES (4,'Arman','Heineking','aheineking3@tuttocitta.it','Male','157.110.61.233')""")
    # cur.execute(
    #     """SELECT * FROM users""")
    # records = cur.fetchall()
    # print(records)
    conn.commit()
    conn.close()


