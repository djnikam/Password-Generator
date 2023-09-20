# Password Generator

from tkinter import *
import string
import random
import pyperclip

def generator():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = s1+s2+s3+s4
    password_length = int(length_Box.get())
    passwordField.delete(0, END)
    if choice.get() == 1:
        passwordField.insert(0, random.sample(s1, password_length))
    if choice.get() == 2:
        passwordField.insert(0, random.sample(s1+s2, password_length))
    if choice.get() == 3:
        passwordField.insert(0, random.sample(s1+s2+s3+s4, password_length))

def copy():
    copied_password=passwordField.get()
    pyperclip.copy(copied_password)

# password = random.sample(s, password_length)
# passwordField.insert(0, password)

root = Tk()
root.geometry('250x375')
root.title('Python Project')
root.config(bg='Gray20')
choice = IntVar()
Font = ('arial', 13, 'bold')

PasswordLabel = Label(root, text='Password Generator', font=('Times New Roman', 20, 'bold'), bg='Gray20', fg='White')
PasswordLabel.grid(pady=10)

weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradiobutton.grid(pady=5)

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradiobutton.grid(pady=5)

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradiobutton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='Gray20', fg='White')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

generateLabel = Button(root, text='Generate', font=Font, bg='Red', fg='White', command=generator)
generateLabel.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(pady=5)

CopyLabel = Button(root, text='Copy', font=Font, bg='Blue', fg='White', command=copy)
CopyLabel.grid(pady=5)

root.mainloop()