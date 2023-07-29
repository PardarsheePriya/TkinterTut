from tkinter import *

root = Tk()
root.geometry("900x600")

#creating frame

#side bar
f1 = Frame(root, bg="grey", borderwidth= 4, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

#top Bar
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")


#Label
l = Label(f1, text="Project Tkinter: Working with Frames")
l.pack(padx= 22, pady= 142)

l2 = Label(f2, text="Welcome to My Text Editor: Menu Bar", font="Poppins")
l2.pack(pady=42)
root.mainloop()