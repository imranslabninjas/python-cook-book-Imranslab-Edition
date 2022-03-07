from tkinter import *
from tkinter.ttk import *

from time import strftime

root = tk()
root.title("clook")
def time():
    string  = strftime("%H,%M,%S")
    label.config(text=string)
    label.after(1000, time)

label = label(root, font=("ds-digital, 80") background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()