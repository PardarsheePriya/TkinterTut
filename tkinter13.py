#dialog Box
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("900x600")
root.title("Message Box")

#function
def myfunc():
    print("This is my function.")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "This is a help for GUI")

def rate():
    print("Rate us")
    val = tmsg.askquestion("Was you experience good?", "You used my GUI. Do you like it?")
    if val == "yes":
        msg = "Great. Rate us on App Store"
    else:
        msg = "Tell us what went wrong. We will call you soon" 
    tmsg.showinfo("Experience", msg)  

#Creating Menu
mainmenu = Menu(root)

#menu 1
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=myfunc)
m1.add_separator()
m1.add_command(label="New Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)

# menu 2
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()
m2.add_command(label="Undo", command=myfunc)

#binding
mainmenu.add_cascade(label="File", menu=m1)
mainmenu.add_cascade(label="Edit", menu=m2)
mainmenu.add_cascade(label="Help", command=help)
mainmenu.add_cascade(label="Rate", command=rate)
mainmenu.add_command(label="Exit", command=quit)

root.config(menu=mainmenu)

root.mainloop()