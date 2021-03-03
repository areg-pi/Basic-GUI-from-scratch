from tkinter import * 

def exit():
    main.destroy()
'''
def register():
    root.title('Access')
    root.geometry("500x400")
    #label1 = Label(root, text = "List", font = ("Helvetica", 18))
    #label1.grid(row=6, column=1)
    root.configure(background = "white")

    # row 1 : the name
    name = Label(root,text="Name: ", font = ("Arial", 13), background = "white")
    name.grid(row=1,column=1)
    name_str = StringVar()
    name_entry = Entry(root,textvariable=name_str, font = ("Times", 18))
    name_entry.grid(row=1,column=2)
    l1 = Label(root, text = '\n', background = "grey", font = ("Arial", 4))

    #row 2 : last name
    last = Label(root,text="Last name: ", font = ("Arial", 13), background = "white")
    last.grid(row=2,column=1)
    last_str = StringVar()
    last_entry = Entry(root,textvariable=last_str, font = ("Times", 18))
    last_entry.grid(row=2,column=2)

    #row 3 : file number
    file = Label(root,text="File number: ", font = ("Arial", 13), background = "white")
    file.grid(row=3,column=1)
    file_str = StringVar()
    file_entry = Entry(root,textvariable=file_str, font = ("Times", 18))
    file_entry.grid(row=3,column=2)

    #row 4 : enter
    enter = Button(root,text="Enter",relief=RIDGE, font = ("Arial", 13), background = "white")
    enter.grid(row=7,column=2)
    
'''
main = Tk()

main.title('Access')
main.geometry("600x500")
main.configure(background = "grey")

l1 = Label(main, text = '\n', background = "grey", font = ("Arial", 4))
l1.pack(side = 'top')
b1 = Button(main, text = "Register", font = ("Arial", 11), width = '20', height = '3')
b1.pack(side = 'top')

l2 = Label(main, text = '\n', background = "grey", font = ("Arial", 3))
l2.pack(side = 'top')
b2 = Button(main, text = "Search", font = ("Arial", 11), width = '20', height = '3')
b2.pack(side = 'top')

l3 = Label(main, text = '\n', background = "grey", font = ("Arial", 3))
l3.pack(side = 'top')
b3 = Button(main, text = "Checklist", font = ("Arial", 11), width = '20', height = '3')
b3.pack(side = 'top')

l4 = Label(main, text = '\n', background = "grey", font = ("Arial", 3))
l4.pack(side = 'top')
b4 = Button(main, text = "Delete", font = ("Arial", 11), width = '20', height = '3')
b4.pack(side = 'top')

l5 = Label(main, text = '\n', background = "grey", font = ("Arial", 3))
l5.pack(side = 'top')
b5 = Button(main, text = "Exit", font = ("Arial", 11), width = '20', height = '3', command = exit)
b5.pack(side = 'top')

main.mainloop()

