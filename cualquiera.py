from tkinter import *
import interface_database_options

root = Tk()


class Window:
   def __init__(self, master, nature):

       self.master = master

       if nature is "MENU":
           self.button = Button(master, text="Register", command=Window.register).grid(row=1, column=0)
           self.button = Button(master, text="Search", command=Window.search).grid(row=2, column=0)
           self.button = Button(master, text="Checklist", command=Window.checklist).grid(row=3, column=0)
           self.button = Button(master, text="Full list", command=Window.full_list).grid(row=4, column=0)
           self.button = Button(master, text="Exit", command=exit).grid(row=7, column=2)

       elif nature is "REGISTER":

           name_entry = Entry(master)
           address_entry = Entry(master)
           file_entry = Entry(master)
           mail_entry = Entry(master)

           def action():
               name = name_entry.get()
               address = address_entry.get()
               file = file_entry.get()
               mail = mail_entry.get()
               interface_database_options.register(interface_database_options.add_user(name, address, file, mail))
               master.destroy()

           self.label = Label(master, text="First name: ").grid(row=2, sticky=W)
           self.label = Label(master, text="Last name: ").grid(row=3, sticky=W)
           self.label = Label(master, text="File number: ").grid(row=4, sticky=W)
           self.label = Label(master, text="E-mail: ").grid(row=5, sticky=W)

           self.button = Button(master, text="Enter", command=action).grid(row=6, column=0)
           self.button = Button(master, text="Cancel", command=master.destroy).grid(row=6, column=1)

           name_entry.grid(row=2, column=1)
           address_entry.grid(row=3, column=1)
           file_entry.grid(row=4, column=1)
           mail_entry.grid(row=5, column=1)

       elif nature is "SEARCH":

           file_entry = Entry(master)

           def action():
               file = file_entry.get()
               name, mail = interface_database_options.search_user(file)
               print("{} --- {}".format(name, mail))
               master.destroy()

           self.label = Label(master, text="File number: ").grid(row=4, sticky=W)

           self.button = Button(master, text="Enter", command=action).grid(row=6, column=0)
           self.button = Button(master, text="Cancel", command=master.destroy).grid(row=6, column=1)

           file_entry.grid(row=4, column=1)

       elif nature is "CHECKLIST":
           pass
#######################################################################################################################

       elif nature is "FULL":
           users = interface_database_options.see_all()
           level = 1
           for row in users:
               level += 1
               self.label = Label(master, text=row).grid(row=level, sticky=W)
#######################################################################################################################

       elif nature is "CONFIRMATION":
           pass

   @staticmethod
   def register():
       rooted = Tk()
       rooted.geometry("500x400")
       rooted.title("Register")
       Window(rooted, 'REGISTER')
       rooted.mainloop()

   @staticmethod
   def search():
       rooted_search = Tk()
       rooted_search.geometry("500x400")
       rooted_search.title("Search")
       Window(rooted_search, 'SEARCH')
       rooted_search.mainloop()

   @staticmethod
   def checklist():
       rooted_check = Tk()
       rooted_check.geometry("500x400")
       rooted_check.title("Checklist")
       Window(rooted_check, 'CHECKLIST')
       rooted_check.mainloop()

   @staticmethod
   def full_list():
       rooted_list = Tk()
       rooted_list.geometry("500x400")
       rooted_list.title("Full list")
       Window(rooted_list, 'FULL')
       rooted_list.mainloop()

   @staticmethod
   def confirmation():
       pass


def main_menu():
   root.geometry("500x400")
   root.title("Access")
   Window(root, 'MENU')
   root.mainloop()


if __name__ == '__main__':
   main_menu()
