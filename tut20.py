from tkinter import *

root = Tk()
root.title("Pardarshee: My GUI")
root.geometry("900x600")

#set icon
root.wm_iconbitmap("icon.ico")

root.configure(background="pink")

width = root.winfo_screenmmwidth()
height = root.winfo_screenmmheight()

print(f"{width} x {height}")
Button(text="Close", padx=18, pady=8, command=root.destroy).pack()

root.mainloop()
