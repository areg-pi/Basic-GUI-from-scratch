from Tkinter import *
root = None
namentry = None
addressentry = None
name = None
address = None
fileentry = None
file = None

def close_window() :
    global name
    global address
    global file
    global nameentry, addressentry, fileentry
    name = nameentry.get()
    address = addressentry.get()
    file = fileentry.get()
    root.destroy()


def DoInputForm(root):
    global nameentry, addressentry, fileentry

    Label(root, text="First name: ").grid(row=2, sticky=W)
    Label(root, text="Last name: ").grid(row=3, sticky=W)
    Label(root, text="File number: ").grid(row=4, sticky=W)

    nameentry = Entry(root)
    addressentry = Entry(root)
    fileentry = Entry(root)

    nameentry.grid(row=2, column=1)
    addressentry.grid(row=3, column=1)
    fileentry.grid(row=4, column=1)

    Button(root, text="Enter", command=close_window).grid(row=5, column=0)
    Button(root, text="Cancel", command=close_window).grid(row=5, column=1)


root = Tk()
root.geometry("500x400")
root.title("Access")
head = Label(root, text = "Hi")
DoInputForm(root)

root.mainloop()