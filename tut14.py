from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("900x600")
root.title("Slides in Tkinter")

def getdol():
    print(f"we have credited {myslider2.get()} dollars to you paypal")

    # Message Box
    msg = f"we have credited {myslider2.get()} dollars to you paypal"
    tmsg.showinfo("credited", msg)

# vertical slider
# myslider = Scale(root, from_=0, to=100)
# myslider.pack()

Label(root, text="How many dollars you want?").pack()
#horizontal slider
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
myslider2.pack()
#button
Button(root, text="Get Dollars",padx=10, pady=10, command=getdol).pack()

root.mainloop()