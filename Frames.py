from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Frames')
root.iconbitmap('icons/frame.ico')

# frame = LabelFrame(root, padx=10, pady=10)
# frame.pack(padx=100, pady=100)

# b = Button(frame, text="Don't Click")
# b2 = Button(frame, text="Don't Click")
# b.grid(row=0, column=0)
# b2.grid(row=1, column=1)

# radio buttons

# var = IntVar()
# var.set('3')

Modes = [
    ("A", "a"),
    ("B", "b"),
    ("C", "c"),
    ("D", "d")
]

char = StringVar()
char.set("a")

for text, mode in Modes:
    Radiobutton(root, text=text, variable=char, value=mode).pack()


def clicked(value, v21):
    global l
    label = Label(root, text=value)
    label.pack()
    l = Label(root, text=v21).pack()


# Radiobutton(root, text='Option 1', variable=var, value=1).pack()
# Radiobutton(root, text='Option 2', variable=var, value=2).pack()
# Radiobutton(root, text='Option 3', variable=var, value=3).pack()
# Radiobutton(root, text='Option 4', variable=var, value=4).pack()


# label = Label(root, text=char.get())
# label.pack()

v2 = IntVar()

c = Checkbutton(root, text="CheckBox", variable=v2)
c.pack()

button = Button(root, text='Click Me!!', command=lambda: clicked(char.get(), v2.get()))
button.pack()

root.mainloop()

