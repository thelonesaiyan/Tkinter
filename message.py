from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.iconbitmap('icons/icon.ico')
root.title('Message Box')


def popup():
    box = messagebox.askyesnocancel("Popup", "Hello, This is Popup!")
    if box == 1:
        Label(root, text='Yes').pack()
    else:
        Label(root, text='No').pack()

button = Button(root, text="Popup", command=popup).pack()

root.mainloop()