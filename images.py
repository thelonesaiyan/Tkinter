from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
# icon addition

root.iconbitmap('icons/image_viewer.ico')

# using images

img1 = ImageTk.PhotoImage(Image.open("images/img.png"))
img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

img_list = [img1, img2, img3, img4, img5]

status = Label(root, text=f'Image 1 / {len(img_list)}', bd=1, relief=SUNKEN)       # anchor=E

label = Label(image=img_list[0])
label.grid(row=0, column=0, columnspan=3)
status.grid(row=1, column=1, sticky=W+E)


def forward(num):
    global label
    global forward_b
    global back_b
    global status

    label.grid_forget()  # forget the previous grid

    label = Label(image=img_list[num])
    status = Label(root, text=f'Image {num+1} / {len(img_list)}', bd=1, relief=SUNKEN)

    forward_b = Button(root, text=">>", command=lambda: forward(num+1))
    back_b = Button(root, text="<<", command=lambda: back(num-1))

    if num == len(img_list)-1:
        forward_b = Button(root, text='>>', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    status.grid(row=1, column=1, sticky=W+E)
    back_b.grid(row=2, column=0)
    forward_b.grid(row=2, column=2)


def back(num):
    global label
    global forward_b
    global back_b
    global status

    label.grid_forget()

    label = Label(image=img_list[num])
    status = Label(root, text=f'Image {num + 1} / {len(img_list)}', bd=1, relief=SUNKEN)

    forward_b = Button(root, text=">>", command=lambda: forward(num + 1))
    back_b = Button(root, text="<<", command=lambda: back(num - 1))

    if num == 0:
        back_b = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    status.grid(row=1, column=1, sticky=W+E)
    back_b.grid(row=2, column=0)
    forward_b.grid(row=2, column=2)

# exit button


back_b = Button(root, text="<<", command=back, state=DISABLED)
button = Button(root, text="Exit", command=root.quit)
forward_b = Button(root, text=">>", command=lambda: forward(1))

back_b.grid(row=2, column=0)
button.grid(row=2, column=1)
forward_b.grid(row=2, column=2, pady=10)

root.mainloop()