from tkinter import *
from tkinter import ttk
prg=Tk()
prg.title("Calculator")
prg.config(background="blue")
screen=Entry(prg,width=24)
screen.grid(row=0, column=1, columnspan=7,pady=2)

exp=""
def click(number):
    global exp

    exp=exp+str(number)
    screen.delete(0,END)
    screen.insert(0,exp)

def equal():
    global exp
    cal=(eval(exp))
    an=(eval(exp))
    screen.delete(0,END)
    screen.insert(0,cal)
    screen.delete(0,END)
    return cal
    

def clear():
    global exp
    screen.delete(0,END)
    exp=""

def ans():
    answ=equal()
    screen.delete(0,END)
    screen.insert(0,answ)

b1=Button(prg,text="1", height=2, width=3, command=lambda:click(1)).grid(row=1, column=1)
b2=Button(prg,text="2", height=2, width=3, command=lambda:click(2)).grid(row=1, column=2)
b3=Button(prg,text="3", height=2, width=3, command=lambda:click(3)).grid(row=1, column=3)
b4=Button(prg,text="+", height=2, width=3, command=lambda:click("+")).grid(row=1, column=4)

b5=Button(prg,text="4", height=2, width=3, command=lambda:click(4)).grid(row=2, column=1)
b6=Button(prg,text="5", height=2, width=3, command=lambda:click(5)).grid(row=2, column=2)
b7=Button(prg,text="6", height=2, width=3, command=lambda:click(6)).grid(row=2, column=3)
b8=Button(prg,text="-", height=2, width=3, command=lambda:click("-")).grid(row=2, column=4)

b9=Button(prg,text="7", height=2, width=3, command=lambda:click(7)).grid(row=3, column=1)
b10=Button(prg,text="8", height=2, width=3, command=lambda:click(8)).grid(row=3, column=2)
b11=Button(prg,text="9", height=2, width=3, command=lambda:click(9)).grid(row=3, column=3)
b12=Button(prg,text="/", height=2, width=3, command=lambda:click("/")).grid(row=3, column=4)

b13=Button(prg,text="0", height=2, width=3, command=lambda:click(0)).grid(row=4, column=1)
b14=Button(prg,text="Clear", height=2, width=3, command=lambda:clear()).grid(row=4, column=2)
b15=Button(prg,text="=", height=2, width=3, command=lambda:equal()).grid(row=4, column=3)
b16=Button(prg,text="*", height=2, width=3, command=lambda:click("*")).grid(row=4, column=4)

Quit=Button(prg, text="Quit", width=5, command=prg.destroy).grid(column=0, row=0)

Ans=Button(prg,text="Ans",width=5, command=lambda:ans()).grid(row=1, column=0)

prg.mainloop()