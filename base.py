from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base Window')
root.iconbitmap('icons/icon.ico')


def open():
    global my_img

    top = Toplevel()
    top.title('New Window')

    my_img = ImageTk.PhotoImage(Image.open('images/img.png'))
    label = Label(top, image=my_img)
    label.pack()

    button2 = Button(top, text='Exit', command=top.destroy).pack()


button = Button(root, text='Open new window', command=open).pack()

root.mainloop()