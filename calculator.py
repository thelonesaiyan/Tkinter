from tkinter import *

root = Tk()
root.title('Calculator')

# hello

equation = Entry(root, width=50, borderwidth=5)
equation.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(number):
    current = equation.get()
    equation.delete(0, END)
    equation.insert(0, str(current) + str(number))


def clear():
    equation.delete(0, END)


def add():
    first = equation.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(float(first))
    equation.delete(0, END)


def sub():
    first = equation.get()
    global f_num
    global math
    math = 'subtract'
    f_num = int(float(first))
    equation.delete(0, END)


def mul():
    first = equation.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(float(first))
    equation.delete(0, END)


def div():
    first = equation.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(float(first))
    equation.delete(0, END)


def equal():
    second = equation.get()
    equation.delete(0, END)
    if math == 'addition':
        equation.insert(0, f_num + int(second))
    elif math == 'subtract':
        equation.insert(0, f_num - int(second))
    elif math == 'multiply':
        equation.insert(0, f_num * int(second))
    elif math == 'divide':
        if int(second) == 0:
            return equation.insert(0, "Divide by 0 Error")
        equation.insert(0, f_num / int(second))
    else:
        equation.delete(0, END)

# Define buttons


butt0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
butt1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
butt2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
butt3 = Button(root, text='3', padx=41, pady=20, command=lambda: click(3))
butt4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
butt5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
butt6 = Button(root, text='6', padx=41, pady=20, command=lambda: click(6))
butt7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
butt8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
butt9 = Button(root, text='9', padx=41, pady=20, command=lambda: click(9))
butt_clear = Button(root, text='C', padx=95, pady=20, command=clear)
butt_eq = Button(root, text='=', padx=95, pady=20, command=equal)
butt_add = Button(root, text='+', padx=39, pady=20, command=add)
butt_sub = Button(root, text='-', padx=41, pady=20, command=sub)
butt_mul = Button(root, text='*', padx=40, pady=20, command=mul)
butt_div = Button(root, text='/', padx=40, pady=20, command=div)

# buttons on screen

butt7.grid(row=1, column=0)
butt8.grid(row=1, column=1)
butt9.grid(row=1, column=2)

butt4.grid(row=2, column=0)
butt5.grid(row=2, column=1)
butt6.grid(row=2, column=2)

butt1.grid(row=3, column=0)
butt2.grid(row=3, column=1)
butt3.grid(row=3, column=2)

butt0.grid(row=4, column=1)
butt_add.grid(row=4, column=0)
butt_sub.grid(row=4, column=2)

butt_clear.grid(row=5, column=1, columnspan=2)
butt_mul.grid(row=5, column=0)

butt_div.grid(row=6, column=0)
butt_eq.grid(row=6, column=1, columnspan=2)

root.mainloop()