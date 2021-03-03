from tkinter import *

check = Tk()

check.title('Checklist')
check.geometry("600x500")
check.configure(background = "white")

q = Label(check,text="\n", font = ("Arial", 3), background = "white")
q.pack(side = TOP)

file = Label(check,text="File number: ", font = ("Arial", 13), background = "white")
file.pack(side = TOP)

p = Label(check,text="\n", font = ("Arial", 5), background = "white")
p.pack(side = TOP)

file_str = StringVar()
file_entry = Entry(check,textvariable=file_str, font = ("Times", 18))
file_entry.pack(side = TOP)
r = Label(check, text = '\n', background = "white", font = ("Arial", 7))
r.pack(side = TOP)

button = Button(check, text = 'Check', font = ('Arial', 13))
button.pack(side = TOP)

check.mainloop()
