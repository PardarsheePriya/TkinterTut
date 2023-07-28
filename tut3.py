from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("900x600")

#storing jpg image
image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)

content = Label(image=photo)
content.pack()
root.mainloop()