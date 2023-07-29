from tkinter import *

root = Tk()
root.geometry("900x600")

#functions
def getVals():
    print("It works!")

#Heading
Label(root, text="Welcome to Travel Form", font="poppins 13 bold").grid(row=0, column=3)

#Text for the Form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
paymentMode = Label(root, text= "Mode of Payment")

#Packing text using Grid Layout
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentMode.grid(row=4, column=2)

#Variable for storing entries of form
nameVal = StringVar()
phoneVal = StringVar()
genderVal = StringVar()
payVal = StringVar()
foodSericeVal = IntVar()

#create entry for dynamic input
nameentry = Entry(root, textvariable=nameVal)
phoneentry = Entry(root, textvariable=phoneVal)
genderentry = Entry(root, textvariable=genderVal)
paymentModeentry = Entry(root, textvariable=payVal)

#packing entry
nameentry.grid(row = 1, column =3)
phoneentry.grid(row = 2, column =3)
genderentry.grid(row = 3, column =3)
paymentModeentry.grid(row =4 , column =3)

#check box
foodSerice = Checkbutton(text="Do you also want to include meals?", variable=foodSericeVal)

#packing checkbox
foodSerice.grid(row=6, column=3)

#button and packing
Button(text="Submitted", command=getVals).grid(row=7, column=3)
root.mainloop()