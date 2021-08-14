
from tkinter import *
from tkinter import ttk 

# Create window
s = Tk()
s.title("Calculator")
so = StringVar()
text = Entry(s).grid(row=0, column=1, columnspan=4)
expression = " "


# Add function
def add(item):
    global expression
    expression += str(item)
    
    

def clear(): 
    global expression 
    expression = "" 
    

def calculate():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    print(result)
    expression = ""
    


# Buttons
ttk.Button(s, text = 7, width=3, command=lambda: add("7")).grid(row=1, column=1, ipady=15)

ttk.Button(s, text = 8, width=3, command=lambda: add("8")).grid(row=1, column=2, ipady=15)

ttk.Button(s, text = 9, width=3, command=lambda: add("9") ).grid(row=1, column=3, ipady=15)

ttk.Button(s, text = '/', width=3, command=lambda: add("/") ).grid(row=1, column=4, ipady=15)

ttk.Button(s, text = 4, width=3, command=lambda: add("4") ).grid(row=2, column=1, ipady=15)

ttk.Button(s, text = 5, width=3, command=lambda: add("5") ).grid(row=2, column=2, ipady=15)

ttk.Button(s, text = 6, width=3, command=lambda: add("6") ).grid(row=2, column=3, ipady=15)

ttk.Button(s, text = 'x', width=3, command=lambda: add("*") ).grid(row=2, column=4, ipady=15)

ttk.Button(s, text = 1, width=3, command=lambda: add("1") ).grid(row=3, column=1, ipady=15)

ttk.Button(s, text = 2, width=3, command=lambda: add("2") ).grid(row=3, column=2, ipady=15)

ttk.Button(s, text = 3, width=3, command=lambda: add("3") ).grid(row=3, column=3, ipady=15)

ttk.Button(s, text = '−', width=3, command=lambda: add("-") ).grid(row=3, column=4, ipady=15)

ttk.Button(s, text = 'C', width=3, command=lambda: clear() ).grid(row=4, column=1, ipady=15)

ttk.Button(s, text = 0, width=3, command=lambda: add("0") ).grid(row=4, column=2, ipady=15)

ttk.Button(s, text = '.', width=3, command=lambda: add(".") ).grid(row=4, column=3 , ipady=15)

ttk.Button(s, text = '+', width=3, command=lambda: add("+") ).grid(row=4, column=4, ipady=15)

ttk.Button(s, text = '=', width=25, command=lambda: calculate() ).grid(row=5, column=1 , ipady=15, columnspan=4)

# Main loop 
s.mainloop()
