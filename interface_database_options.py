from students import Students
import interface_database_configuration

conn, c = interface_database_configuration.create_connection()
interface_database_configuration.create_table(c)


def register(person):
   with conn:
       c.execute("INSERT INTO students VALUES (:first, :last, :expedient, :mail)",
                 {'first': person.first, 'last': person.last, 'expedient': person.expedient, 'mail': person.mail})


def add_user(first, last, expedient, mail):
   new_user = Students(first, last, expedient, mail)
   return new_user


def search_user(expedient):
   c.execute("SELECT first, last, expedient, mail FROM students WHERE expedient=:expedient", {'expedient': expedient})
   data = c.fetchone()
   if data is None:
       message = "Not found."
       alternative = "None."
       return message, alternative
   else:
       full_name = data[0] + " " + data[1]
       mail = data[3]
       return full_name, mail


def erase_user():
   pass


def see_all():
   c.execute("SELECT * FROM students")
   rows = c.fetchall()
   return rows
