#Buttons 

from tkinter import *
root = Tk()
root.geometry("900x600")

#function
def hello():
    print("Hello, From Tkinter Buttons")


def name():
    print("The name is Pardarshee Priya")

def likes():
    print("I like tkinter Python")

#creating frame
frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

#creating button
b1 = Button(frame, fg="red", text="Print Now", command= hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me Name", command=name)
b2.pack(side= LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print Now", command=likes)
b3.pack(side=LEFT, padx=23)
root.mainloop()