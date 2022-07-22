from tkinter import *

Sparsh_Root = Tk()
Sparsh_Root.geometry("720x480")

def CALCULATE():
    a = float(A_ENTRY.get())
    b = float(B_ENTRY.get())
    c = float(C_ENTRY.get())
    answer_1 = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
    answer_2 = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)

    ANSWER_LABEL = Label(Sparsh_Root, text = f"The solutions for the equation are {answer_1} and {answer_2}", font = ('Verdana 15 italic'))
    ANSWER_LABEL.pack()

TITLE = Label(Sparsh_Root, text = "QUADRATIC EQUATION SOLVER", font = ('Verdana 24 bold underline'))
TITLE.pack()

DESCRIPTION = Label(Sparsh_Root, text = "Any quadratic equation is in the form ax^2 + bx + c.\nInput the values of a, b and c to get the solution(s).", font = ('Bahnschrift 18 bold'))
DESCRIPTION.pack()

A = Label(Sparsh_Root, text = "Enter the value of 'a' : ", font = ('Corbel 15 italic'))
A.pack()

A_ENTRY = Entry(Sparsh_Root)
A_ENTRY.pack()

B = Label(Sparsh_Root, text = "Enter the value of 'b' : ", font = ('Corbel 15 italic'))
B.pack()

B_ENTRY = Entry(Sparsh_Root)
B_ENTRY.pack()

C = Label(Sparsh_Root, text = "Enter the value of 'c' : ", font = ('Corbel 15 italic'))
C.pack()

C_ENTRY = Entry(Sparsh_Root)
C_ENTRY.pack()

CALCULATE_BUTTON = Button(Sparsh_Root, text = "Find Solution(s)", font = ('Bahnschrift 15'), bg = 'red', fg = 'yellow', activebackground = 'blue', command = CALCULATE)
CALCULATE_BUTTON.pack()

Sparsh_Root.mainloop()
