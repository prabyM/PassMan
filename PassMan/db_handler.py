import sqlite3
import os

file_present = os.path.isfile("credentials.db")

if file_present is False:
    try:
        open('credentials.db', 'w').close()
    except Error as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()




