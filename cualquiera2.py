from tkinter import *
import interface_database_options

root = Tk()
root.configure(background='white')

class Window:
   def __init__(self, master, nature):

       self.master = master

       if nature is "MENU":
           self.button = Button(master, text="Register", command=Window.register, font = ('Arial',13), width = 20, height = 2).place(x=150, y=40)
         # self.button = Button(master, text="Search", command=Window.search, font = ('Arial',13)).place(x=210, y=80)
           self.button = Button(master, text="Checklist", command=Window.checklist, font = ('Arial',13), width = 20, height = 2).place(x=150, y=120)
         # self.button = Button(master, text="Full list", command=Window.full_list, font = ('Arial',13)).place(x=210, y=160)
           self.button = Button(master, text="Delete", command=Window.delete, font = ('Arial',13), width = 20, height = 2).place(x=150, y=200)
           self.button = Button(master, text="Exit", command=exit, font = ('Arial',13), width = 20, height = 2, bg = 'IndianRed1').place(x=150, y=280)

       elif nature is "REGISTER":

           name_entry = Entry(master, width=25, font = ('Arial',12))
           address_entry = Entry(master, width=25, font = ('Arial',12))
           file_entry = Entry(master, width=25, font = ('Arial',12))
           mail_entry = Entry(master, width=25, font = ('Arial',12))

           def action():
               name = name_entry.get()
               address = address_entry.get()
               file = file_entry.get()
               mail = mail_entry.get()
               interface_database_options.register(interface_database_options.add_user(name, address, file, mail))
               master.destroy()

           master.configure(background='white')
           self.label = Label(master, text = "Registration", font = ('Arial', 18), bg = 'white').place(x=190, y=40)
           self.label = Label(master, text="First name:", font = ('Arial',13), bg = 'white').place(x=70, y=130)
           self.label = Label(master, text="Last name:", font = ('Arial',13), bg = 'white').place(x=70, y=180)
           self.label = Label(master, text="File number:", font = ('Arial',13), bg = 'white').place(x=70, y=230)
           self.label = Label(master, text="E-mail:", font = ('Arial',13), bg = 'white').place(x=70, y=280)

           self.button = Button(master, text="Sign up", bg = 'blue', fg = 'white', width = 10, height = 1, command=action, font = ('Arial',12)).place(x=130, y=370)
           self.button = Button(master, text="Cancel", width = 10, height = 1, command=master.destroy, font = ('Arial',12)).place(x=300, y=370)

           name_entry.place(x=200, y=130)
           address_entry.place(x=200, y=180)
           file_entry.place(x=200, y=230)
           mail_entry.place(x=200, y=280)

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

       elif nature is "DELETE":

           file_entry = Entry(master, width=25, font = ('Arial',12))

           def action():
              
               file = file_entry.get()
               
               interface_database_options.register(interface_database_options.add_user(name, address, file, mail))
               master.destroy()

           master.configure(background='white')
           self.label = Label(master, text = "Delete student", font = ('Arial', 18), bg = 'white').place(x=175, y=40)
           self.label = Label(master, text= "File number:", font = ('Arial',13), bg = 'white').place(x=70, y=180)

           self.button = Button(master, text="Delete", bg = 'red', fg = 'white', width = 10, height = 1, command=action, font = ('Arial',12)).place(x=130, y=300)
           self.button = Button(master, text="Cancel", width = 10, height = 1, command=master.destroy, font = ('Arial',12)).place(x=280, y=300)

           file_entry.place(x=200, y=180)
           
       elif nature is "CONFIRMATION":
           pass

   @staticmethod
   def register():
       rooted = Tk()
       rooted.geometry("500x500")
       rooted.title("Register")
       Window(rooted, 'REGISTER')
       rooted.mainloop()

   @staticmethod
   def search():
       rooted_search = Tk()
       rooted_search.geometry("500x500")
       rooted_search.title("Search")
       Window(rooted_search, 'SEARCH')
       rooted_search.mainloop()

   @staticmethod
   def checklist():
       rooted_check = Tk()
       rooted_check.geometry("500x500")
       rooted_check.title("Checklist")
       Window(rooted_check, 'CHECKLIST')
       rooted_check.mainloop()

   @staticmethod
   def full_list():
       rooted_list = Tk()
       rooted_list.geometry("500x500")
       rooted_list.title("Full list")
       Window(rooted_list, 'FULL')
       rooted_list.mainloop()

   @staticmethod
   def delete():
       rooted_delete = Tk()
       rooted_delete.geometry("500x500")
       rooted_delete.title("Delete")
       Window(rooted_delete, 'DELETE')
       rooted_delete.mainloop()

   @staticmethod
   def confirmation():
       pass


def main_menu():
   root.geometry("500x500")
   root.title("Access")
   Window(root, 'MENU')
   root.mainloop()


if __name__ == '__main__':
   main_menu()
