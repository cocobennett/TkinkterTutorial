from tkinter import *

window = Tk()

window.title("Welcome")

window.geometry('350x200')

lbl = Label(window, text="Hello World")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button clicked!")

btn = Button(window, text="Click Me", command=clicked, bg="Magenta", fg="White")

btn.grid(column=0, row=1)

window.mainloop()
