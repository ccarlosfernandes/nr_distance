#!/usr/bin/env python3

import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)

entry.pack()

name = entry.get()

print(name)


top = tk.Tk()

Lb1 = tk.Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")



Lb1.pack()



master = tk.Tk()

variable = tk.StringVar(master)
variable.set("one") # default value

w = tk.OptionMenu(master, variable, "one", "two", "three")
w.pack()

master.mainloop()



top.mainloop()

window.mainloop()