#Radio Buttons
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("900x600")
root.title("Radio Button in Tkinter")

#function
def order():
    tmsg.showinfo("Order Received", f"Thank you Ordering. Your {var.get()} will be delivered soon")

# var = IntVar()
var = StringVar()
var.set(1)  #can set value using set func
Label(root, text="What would you like to eat?", justify=LEFT, padx=14, font="lucida 19 bold").pack()

#radio button
radio = Radiobutton(root, text="Dosa", font="poppins, 12 bold", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Noodles", font="poppins, 12 bold", padx=14, variable=var, value="Noodles").pack(anchor="w")
radio = Radiobutton(root, text="Indian Thali", font="poppins, 12 bold", padx=14, variable=var, value="Indian Thali").pack(anchor="w")
radio = Radiobutton(root, text="Pizza", font="poppins, 12 bold", padx=14, variable=var, value="Pizza").pack(anchor="w")
radio = Radiobutton(root, text="Burger", font="poppins, 12 bold", padx=14, variable=var, value="Burger").pack(anchor="w")


Button(text="Order Now", padx= 10, pady=10, command=order).pack()
root.mainloop()