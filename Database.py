from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databse")
root.geometry("400x400")

# Database


def submit():
    # clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    add.delete(0, END)
    cit.delete(0, END)
    stat.delete(0, END)
    zi.delete(0, END)

    # Create
    conn = sqlite3.connect('address.db')

    # cursor instance
    cur = conn.cursor()

    # Insert Query
    '''cur.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")'''

    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :add, :cit, :stat, :zi)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'add': add.get(),
                    'cit': cit.get(),
                    'stat': stat.get(),
                    'zi': zi.get()
                })

    # cur.execute('DROP TABLE addresses')

    # commit changes
    conn.commit()

    # close database
    conn.close()


def Pull():
    # Create
    conn = sqlite3.connect('address.db')

    # cursor instance
    cur = conn.cursor()

    cur.execute('SELECT *, oid FROM addresses')
    records = cur.fetchall()              # fetchone(), fetchmany(range)

    print(records)
    rec = ''
    for record in records:
        rec += str(record) + '\n'

    lab = Label(root, text=rec)
    lab.grid(row=8, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close database
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

add = Entry(root, width=30)
add.grid(row=2, column=1, padx=20)

cit = Entry(root, width=30)
cit.grid(row=3, column=1, padx=20)

stat = Entry(root, width=30)
stat.grid(row=4, column=1, padx=20)

zi = Entry(root, width=30)
zi.grid(row=5, column=1, padx=20)

f = Label(root, text=" First Name: ")
f.grid(row=0, column=0, padx=20)

l = Label(root, text=" Last Name: ")
l.grid(row=1, column=0, padx=20)

a = Label(root, text=" Address: ")
a.grid(row=2, column=0, padx=20)

c = Label(root, text=" City: ")
c.grid(row=3, column=0, padx=20)

s = Label(root, text=" State: ")
s.grid(row=4, column=0, padx=20)

z = Label(root, text=" Zip Code: ")
z.grid(row=5, column=0, padx=20)

# create submit button
sub = Button(root, text='Submit', command=submit)
sub.grid(row=6, column=0, columnspan=2, pady = 10, padx=10, ipadx=100)


pull = Button(root, text ='Print', command=Pull)
pull.grid(row=7, column=0, columnspan=2, pady = 10, padx=10, ipadx=100)
root.mainloop()
