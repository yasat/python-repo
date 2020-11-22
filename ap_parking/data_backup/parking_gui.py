from tkinter import *
import tkinter as tk
main=tk.Tk()
main.title('Airport Parking')
Label(main,text='vehicle number: ').grid(row=0)
e1=Entry(main)
e1.grid(row=0,column=1)
but=tk.Button(main, text='test')
but.pack()
main.mainloop()

def test_fun():
    print("testing")
