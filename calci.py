import tkinter as tk
import math

def on_click(button_Text):
    if button_Text == "C":
        clearing()
    elif button_Text == "=":
        calculation()
    elif button_Text == "<-":
        backspace()
    elif button_Text == "sqrt":
        squareroot()
    else:
        displaying(button_Text)

def calculation():
    try:
        expressions = display.get()
        expressions = expressions.replace("!", "factorial")
        answer = eval(expressions)
        display.delete(0, tk.END)
        display.insert(tk.END, str(answer))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, e) 

def squareroot():
    expressions = display.get()
    try:
        number = float(expressions)
        answer = math.sqrt(number)
        display.delete(0, tk.END)  # Clear the current display content
        display.insert(tk.END, str(answer))
    except ValueError:
      display.delete(0, tk.END)
      display.insert(tk.END, e) 

def displaying(button_Text):
    currentvalue = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, currentvalue + button_Text)

def clearing():
    display.delete(0, tk.END)

def backspace():
    currentvalue = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, currentvalue[:-1])

#creating a window
mainwindow= tk.Tk()
#assigning the heading
mainwindow.title("Calculator")

# Create the display of the window
display = tk.Entry(mainwindow, width=20, justify=tk.LEFT, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define the button layout text,row,col
buttons_cal = [
    ("C", 1, 0), ("sqrt", 1, 1), ("/", 1, 2), ("<-", 1, 3), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3), 
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), 
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("!", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

# Create buttons
for buttons_text, rows, cols in buttons_cal:
    button = tk.Button(mainwindow, text=buttons_text, padx=10, pady=10, font=("Arial", 15), command = lambda button_Text = buttons_text: on_click(button_Text))
    button.grid(row=rows, column=cols, padx=5, pady=5)

#This starts the main event loop of the application, allowing it to respond to user interactions and events.
mainwindow.mainloop()
