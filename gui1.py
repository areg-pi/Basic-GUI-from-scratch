from Tkinter import *

root = Tk()

root.title('Access')
root.geometry("500x400")
#label1 = Label(root, text = "List", font = ("Helvetica", 18))
#label1.grid(row=6, column=1)
root.configure(background = "white")

# row 1 : the name
name = Label(root,text="Name: ", font = ("Times", 18), background = "white")
name.grid(row=1,column=1)
name_str = StringVar()
name_entry = Entry(root,textvariable=name_str, font = ("Times", 18))
name_entry.grid(row=1,column=2)

#row 2 : last name
last = Label(root,text="Last name: ", font = ("Times", 18), background = "white")
last.grid(row=2,column=1)
last_str = StringVar()
last_entry = Entry(root,textvariable=last_str, font = ("Times", 18))
last_entry.grid(row=2,column=2)

#row 3 : file number
file = Label(root,text="File number: ", font = ("Times", 18), background = "white")
file.grid(row=3,column=1)
file_str = StringVar()
file_entry = Entry(root,textvariable=file_str, font = ("Times", 18))
file_entry.grid(row=3,column=2)

#row 4 : enter
enter = Button(root,text="Enter",relief=RIDGE, font = ("Times", 15), background = "white")
enter.grid(row=7,column=2)

root.mainloop()