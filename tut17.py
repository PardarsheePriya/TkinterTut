#Scroll Bar
from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Scroll Bar in Tkinter")
#for connecting scrollbar to widget - steps
#1. widget(yscrollcommand = scrollbar.set)
#3. scrollbar.config(commmand = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT, fill= Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(350):
    listbox.insert(END, f"Item {i}")

listbox.pack(fill="both", padx=30)
scrollbar.config(command=listbox.yview)
root.mainloop()