import _tkinter
import tkinter
from tkinter import messagebox

thingy = tkinter.Tk()

def askForBeans():
    messagebox.showinfo("BEANS","It is bean time")

B = tkinter.Button(text="start", command=askForBeans)

B.pack()
thingy.mainloop()
