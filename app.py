from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

idValue = StringVar()
nameValue = StringVar()
passwordValue = StringVar()
surnameValue = StringVar()
addressValue = StringVar()
commentsValue = StringVar()
db_connection = sqlite3.connect('crudBD')
def connection():

    try:


        db_connection.execute("""CREATE TABLE users_data (
                        id int(60) PRIMARY_KEY AUTO_INCREMENT,
                        ) """)

    except ConnectionError:
        messagebox.ERROR("something goes bad")

def exitProgram():
    close = messagebox.askokcancel("Are you sure you want to exit?", "If you press ok program will close")

    if close:
        root.destroy()


def clearFields():
    idValue.set("")
    nameValue.set("")
    passwordValue.set("")
    surnameValue.set("")
    addressValue.set("")
    commentsValue.set("")




# -----menu--------

menuBar = Menu(root)

dbMenu = Menu(menuBar, tearoff=0)

dbMenu.add_command(label="Connect", command=lambda: connection)
dbMenu.add_command(label="Exit", command=exitProgram)

deleteMenu = Menu(menuBar, tearoff=0)

deleteMenu.add_command(label="Delete fields", command=clearFields)

crudMenu = Menu(menuBar, tearoff=0)

crudMenu.add_command(label="Create", command=lambda: create)
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

helpMenu = Menu(menuBar, tearoff=0)

helpMenu.add_command(label="License")
helpMenu.add_command(label="About")

menuBar.add_cascade(label="DB", menu=dbMenu)
menuBar.add_cascade(label="Delete", menu=deleteMenu)
menuBar.add_cascade(label="CRUD", menu=crudMenu)
menuBar.add_cascade(label="Help", menu=helpMenu)

# -------Form-------

idLabel = Label(text="id").grid(row=1, column=2, pady=9, padx=9)
name = Label(text="name").grid(row=2, column=2, pady=9, padx=9)
password = Label(text="password").grid(row=3, column=2, pady=9, padx=9)
surname = Label(text="surname").grid(row=4, column=2, pady=9, padx=9)
address = Label(text="address").grid(row=5, column=2, pady=9, padx=9)
comments = Label(text="comments").grid(row=6, column=2, pady=9, padx=9)

idEntry = Entry(root, textvariable=idValue).grid(row=1, column=3, pady=9, padx=9)
nameEntry = Entry(root, textvariable=nameValue).grid(row=2, column=3)
passwordEntry = Entry(root, textvariable=passwordValue, show="*").grid(row=3, column=3)
surnameEntry = Entry(root, textvariable=surnameValue).grid(row=4, column=3)
addressEntry = Entry(root, textvariable=addressValue).grid(row=5, column=3)
commentsEntry = Text(root, width=18, height=5).grid(row=6, column=3)


# -----btn-----

btnCreate = Button(root, text="create").grid(row=7, column=2, pady=14, sticky="w", padx=6)
btnRead = Button(root, text="read").grid(row=7, column=2, columnspan=2, pady=14, padx=34)
btnUpdate = Button(root, text="update").grid(row=7, column=3, columnspan=6, pady=14)
btnDelete = Button(root, text="delete").grid(row=7, column=3, pady=14, sticky="e")

root.config(menu=menuBar)
root.geometry("400x400")
root.mainloop()
