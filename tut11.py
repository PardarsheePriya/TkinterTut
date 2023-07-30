#Handling events in Tkinter GUI

from tkinter import *

root = Tk()
root.title("Events Handling")
root.geometry("900x600")

#function
def pardarshee(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

widget = Button(root, text="Click me")
widget.pack()

widget.bind('<Button-1>', pardarshee)
root.mainloop()