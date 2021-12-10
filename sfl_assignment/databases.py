from pathlib import Path

import sqlite3



def sqlite_connection_factory():
    path = Path.home().joinpath('.sfl_assignment', 'users.db')
    conn = sqlite3.connect(str(path))
    return conn


def build_users_db(database: str):
    connection_factory = DATABASES[database]
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

    conn.commit()
    conn.close()


DATABASES = {
    'sqlite': sqlite_connection_factory
}
