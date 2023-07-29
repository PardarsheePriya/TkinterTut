#Grid Layout
from tkinter import *

root = Tk()
root.geometry("900x600")

#functions
def getval():
    print(uservalue.get())
    print(passvalue.get())

user = Label(root, text="User name")
password = Label(root, text="Password")

user.grid()
password.grid(row=1)


#Entry Widget: we can add values dynamically
# Variable classes in TKinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

#Button
Button(text="Submit", command=getval).grid()
root.mainloop()