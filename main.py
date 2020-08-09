from tkinter import *

root = Tk()  # working with tkinter

# Creating a label widget
# label = Label(root, text='Hello World!')    # .grid(row=0, column=0)
# label1 = Label(root, text='Hello')          # .grid(row=10, column=10)

# Showing it to the screen
# label.grid(row=0, column=0)
# label1.grid(row=10, column=10)

# creating button


# def myfunc():
    # mylabel = Label(root, text='Clicked a button')
    # mylabel.pack()


# button = Button(root, text='Click Me!', command=myfunc, fg='#000000', bg='gray')     # state=DISABLED,  padx=50, pady=50
# button.pack()

# root.mainloop()

entry = Entry(root, width=50, borderwidth=10, bg='#000000', fg='white')
entry.pack()
entry.insert(0, "Enter your name: ")


def onclick():
    label = Label(root, text=entry.get())
    label.pack()


name_button = Button(root, text='Click Me!', bg='white', fg='black', command=onclick)
name_button.pack()

root.mainloop()