#Menus and Sub Menus

from tkinter import *
root = Tk()
root.geometry("900x600")
root.title("Menus and Submenus")

#function
def myfunc():
    print("this is my function. Pardarshee made me")


#Use these to create a non drop down menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)

dropmenu = Menu(root)
m1 = Menu(dropmenu)
m1.add_command(label="New File", command=myfunc)
m1.add_separator()
m1.add_command(label="New Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)

#edit menu
m2 = Menu(dropmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Add", command=myfunc)

dropmenu.add_cascade(label="File", menu=m1)
dropmenu.add_cascade(label="Edit", menu=m2)
dropmenu.add_command(label="Exit", command=quit)

root.config(menu=dropmenu)

root.mainloop()