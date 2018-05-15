# Code is from Udemy: "The Python Mega Course: Build 10 Real World Applications" by Ardit Sulce

from tkinter import *

window=Tk()

def kg_converter():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END,grams)
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    t3.delete("1.0", END)
    t3.insert(END,ounces)

b1=Button(window,text="Convert",command=kg_converter)
b1.grid(row=0, column=2)

e0=Label(window,text="Kg")
e0.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

l1=Label(window,text="Grams")
l1.grid(row=1,column=0)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=1)

l2=Label(window,text="Pounds")
l2.grid(row=2,column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=2, column=1)

l3=Label(window,text="Ounces")
l3.grid(row=3,column=0)

t3=Text(window, height=1, width=20)
t3.grid(row=3, column=1)

window.mainloop()
