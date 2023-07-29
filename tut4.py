from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("My GUI by Pardarshee")

#Lable Options
# text - add the Text
# bd - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling (SUNKEN, RAISED, GROOVE, RIDGE )

title_label = Label(text="The sun had just risen, casting a warm \ngolden glow across the tranquil meadow. Birds chirped joyfully, \ncelebrating the beginning of a new day. A gentle breeze rustled \nthrough the leaves of the tall oak trees, creating a soothing \nmelody. As I walked along the narrow path, the scent of \nwildflowers filled the air, intoxicating my senses. In the \ndistance, a babbling brook flowed gracefully, adding to the\n serenity of the scene. Nature seemed to be waking up, welcoming me \nto embrace its beauty.", bg = "pink", fg = "black", padx = 113, pady= 94, font="poppins 19 bold")

title_label.pack()
root.mainloop()