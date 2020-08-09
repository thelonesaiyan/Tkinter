from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Slider Window')
root.geometry("400x400")        # size of window to 400x400


def slide():
    lab = Label(root, text=hori.get()).pack()
    root.geometry(f"{hori.get()}x{slid.get()}")


slid = Scale(root, from_=0, to=200)
slid.pack()

hori = Scale(root, from_=0, to=200, orient=HORIZONTAL)
hori.pack()

btn = Button(root, text='Look Me', command=slide).pack()

root.mainloop()