import tkinter as Tk
import tkinter.ttk as Ttk

window = Tk.Tk()

window.title("Welcome")

window.geometry('350x200')

combo = Ttk.Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=1, row=1)

lbl = Tk.Label(window, text="Hello World")

lbl.grid(column=1, row=0)

input = Tk.Entry(window, width = 10)

input.grid(column=0, row=1)

input.focus()

def clicked():
    res = f"Welcome to {input.get()}"
    lbl.configure(text=res)

btn = Tk.Button(window, text="Click Me", command=clicked, bg="Magenta", fg="White")

btn.grid(column=0, row=0)

window.mainloop()
