import sqlite3


def create_connection():
   connection = sqlite3.connect(':memory:')
   cursor = connection.cursor()
   return connection, cursor


def create_table(cursor):
   cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               first text,
               last text,
               expedient text,
               mail text
               )""")


def closure(connection, cursor):
   cursor.close()
   connection.close()
