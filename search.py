from tkinter import *

search = Tk()

search.title('Search')
search.geometry("500x400")
#label1 = Label(search, text = "List", font = ("Helvetica", 18))
#label1.grid(row=6, column=1)
search.configure(background = "white")

# row 1 : the name
name = Label(search,text="Name: ", font = ("Arial", 13), background = "white")
name.grid(row=1,column=1)
name_str = StringVar()
name_entry = Entry(search,textvariable=name_str, font = ("Times", 18))
name_entry.grid(row=1,column=2)
l1 = Label(search, text = '\n', background = "grey", font = ("Arial", 4))

#row 2 : last name
last = Label(search,text="Last name: ", font = ("Arial", 13), background = "white")
last.grid(row=2,column=1)
last_str = StringVar()
last_entry = Entry(search,textvariable=last_str, font = ("Times", 18))
last_entry.grid(row=2,column=2)

#row 3 : file number
file = Label(search,text="File number: ", font = ("Arial", 13), background = "white")
file.grid(row=3,column=1)
file_str = StringVar()
file_entry = Entry(search,textvariable=file_str, font = ("Times", 18))
file_entry.grid(row=3,column=2)

#row 4 : enter
buscar = Button(search,text="Search",relief=RIDGE, font = ("Arial", 13), background = "white")
buscar.grid(row=7,column=2)

search.mainloop()
