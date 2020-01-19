from tkinter import *
import tkinter as tk
import tkinter.messagebox

def add():
    try:
        answer=0
        E4.delete(0,'end')
        num1 = int(Entry.get(E1))
        num2 = int(Entry.get(E2))
        E4.config(state='normal')
        answer = num1+num2
    except:
        messagebox.showwarning("Warning","Enter number only..")
        answer="ValueError"
    Entry.insert(E4,0,answer)
    print(answer)
    
def sub():
    try:
        E4.delete(0,'end')
        answer=0
        num1 = int(Entry.get(E1))
        num2 = int(Entry.get(E2))
        E4.config(state='normal')
        answer = num1-num2
    except:
        messagebox.showwarning("Warning","Enter number only..")
        answer="ValueError"
    Entry.insert(E4,0,answer)
    print(answer)
    
def prod():
    try:
        answer=0
        E4.delete(0,'end')
        num1 = int(Entry.get(E1))
        num2 = int(Entry.get(E2))
        E4.config(state='normal')
        answer = num1*num2
    except:
        messagebox.showwarning("Warning","Enter number only..")
        answer="ValueError"
    Entry.insert(E4,0,answer)
    print(answer)

def div():
    try:
        answer=0
        E4.delete(0,'end')
        num1 = int(Entry.get(E1))
        num2 = int(Entry.get(E2))
        E4.config(state='normal')
        try:
            answer=num1/num2
        except:
            answer = "Error: Division by 0"
            messagebox.showwarning("Warning","Division by Zero error..")
    except:
        messagebox.showwarning("Warning","Enter number only..")
        answer="ValueError"
    Entry.insert(E4,0,answer)
    print(answer)
    
top = tkinter.Tk()
top.title("Calculator")
L1 = Label(top, text="My calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L5 = Label(top, text="Answer",).grid(row=3,column=0)
E1 = Entry(top, bd =3)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =3)
E2.grid(row=2,column=1)

E4 = Entry(top, bd =3,state='disabled')
E4.grid(row=3,column=1)
B1= Button(top, text ="+",command = add).grid(row=4,column=1,columnspan = 2,sticky = tk.W + tk.E)
B2 = Button(top, text ="-",command = sub).grid(row=1,column=2)
B3 = Button(top, text ="*",command = prod).grid(row=2,column=2)
B4 = Button(top, text ="/",command = div).grid(row=3,column=2)
top.mainloop()