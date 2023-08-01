#Status Bar

from tkinter import *

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.title("Status Bar")
root.geometry("900x600")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

#button
Button(root, text="Upload", padx= 22, pady=22, relief=SUNKEN, command=upload).pack()
root.mainloop()