from tkinter import *

root = Tk()
root.configure(background = 'white')
root.geometry('500x500')

frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(root, text = 'Name').place(x = 100, y = 100)
label2 = Label(frame1, text = 'Last name').place(x = 100, y = 200)
label3 = Label(frame1, text = 'File').place(x = 100, y = 300)

entry1 = Entry(frame1).place(x = 200, y = 100)
entry2 = Entry(frame1).place(x = 200, y = 200)
entry3 = Entry(frame1).place(x = 200, y = 300)

button1 = Button(frame1, text = 'Bye')

########################################################################

label4 = Label(frame2, text = 'Bitch')
label5 = Label(frame2, text = 'Son')
label6 = Label(frame2, text = 'of')

entry4 = Entry(frame2)
entry5 = Entry(frame2)
entry6 = Entry(frame2)

button2 = Button(frame2, text = 'jeje')

root.mainloop()

