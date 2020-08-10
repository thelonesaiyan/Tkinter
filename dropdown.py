from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Drop Down Menu')
root.geometry("400x400")

clicked = StringVar()
clicked.set("Monday")


def show():
    label = Label(root, text=clicked.get()).pack()


drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
drop.pack()

butt = Button(root, text='Show selection', command=show).pack()

root.mainloop()