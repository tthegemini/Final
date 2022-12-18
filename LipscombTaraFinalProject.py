#Name: Tara Lipscomb
#Final Project: 4 Function Calculator


from tkinter import *

#calculations for adding, subtracting, multiplying and dividing user entered numbers

def add_numbers():
    res=float(e1.get()) + float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

def subtract_numbers():
    res=float(e1.get()) - float(e2.get())
    lab4.config(text=res)

def multiply_numbers():
    res=float(e1.get())*float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

def divide_numbers():
    res=float(e1.get()) / float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

    


#start of main project

window=Tk()

#laying out the calculators window
#entry label creation
window.title('Python 4 Function Calculator')
canvas=Canvas(window, width=1000, height=500)

lab1=Label(window, text="Enter 1st Number:")
lab1.grid(row=0, column=0)
lab2=Label(window, text="Enter 2nd Number:")
lab2.grid(row=1, column=0)
lab3=Label(window, text="Result:")
lab3.grid(row=2, column=0)
lab4=Label(window, text="")
lab4.grid(row=2, column=1)

e1=Entry(window)
e2=Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#button creation

b1=Button(window, text="Add", width=10, command=add_numbers)
b1.grid(row=0, column=2, padx=5, pady=5)

b2=Button(window, text="Subtract", width=10, command=subtract_numbers)
b2.grid(row=0, column=3, padx=5, pady=5)

b3=Button(window, text="Multiply", width=10, command=multiply_numbers)
b3.grid(row=1, column=2, padx=5, pady=5)

b4=Button(window, text="Divide", width=10, command=divide_numbers)
b4.grid(row=1, column=3, padx=5, pady=5)

b5=Button(window, text="Exit", width=10, command=window.destroy)
b5.grid(row=2, column=2, padx=5, pady=5)
