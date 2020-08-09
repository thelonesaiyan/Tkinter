from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('icons/icon.ico')
root.title('Select Files')


def open():
    global label
    global img
    
    root.filename = filedialog.askopenfilename(initialdir="D:\Py_udemy\\tkinter\images", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img.label = Label(image=img).pack()


but = Button(root, text="Open Files", command=open)
but.pack()

root.mainloop()