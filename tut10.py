from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Geometry with Pardarshee")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#The line goes from points x1, y1 to x2, y2
can_widget.create_line(0, 200, 800, 0, fill="blue")
can_widget.create_line(800, 200, 0, 0, fill="red")

#top left to bottom coordinate
can_widget.create_rectangle(30, 50, 700, 300)

#Adding text with it's defined position
can_widget.create_text(200, 200, text="This is Pardarshee Drawing", fill="green", font="poppins")

#adding oval
can_widget.create_oval(50, 50, 150, 300)
root.mainloop()