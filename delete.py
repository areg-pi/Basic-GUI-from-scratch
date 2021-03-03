from tkinter import *

delete = Tk()

delete.title('Delete')
delete.geometry("600x500")
delete.configure(background = "white")

q = Label(delete,text="\n", font = ("Arial", 3), background = "white")
q.pack(side = TOP)

file = Label(delete,text="File number: ", font = ("Arial", 13), background = "white")
file.pack(side = TOP)

p = Label(delete,text="\n", font = ("Arial", 5), background = "white")
p.pack(side = TOP)

file_str = StringVar()
file_entry = Entry(delete,textvariable=file_str, font = ("Times", 18))
file_entry.pack(side = TOP)
r = Label(delete, text = '\n', background = "white", font = ("Arial", 7))
r.pack(side = TOP)

button = Button(delete, text = 'Delete', font = ('Arial', 13))
button.pack(side = TOP)

delete.mainloop()
