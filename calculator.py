import tkinter as tk

# Create the main window
root = tk.Tk()
root.title = "Calculator"  # Set the window title
root.configure(background="black")  # Set the background color of the main window

# Create the display entry widget to show user input and results
display = tk.Entry(root, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

# Initialize global variables for calculations
n1 = 0  # First number
n2 = 0  # Second number
operator = ""  # Stores the selected operator (+, -, *, /)


def clear():
    """Clears the display and resets calculation variables."""
    display.delete(0, tk.END)
    global n1, n2, operator
    n1 = 0
    n2 = 0
    operator = ""


def update_display(number):
    """Updates the display with the given number."""
    current_val = display.get()  # Get the current value from the display
    display.delete(0, tk.END)  # Clear the display
    display.insert(0, current_val + number)  # Append the new number to the current value


def clearFirstNumber(t):
    """Saves the first number and clears the display for the second number.
    
    Args:
        t (str): The operator selected (+, -, *, /).
    """
    global n1, operator
    n1 = int(display.get())  # Store the first number
    display.delete(0, tk.END)  # Clear the display
    operator = t  # Save the operator


def addNumbers():
    """Performs addition and updates the display."""
    result = n1 + n2
    display.delete(0, tk.END)
    display.insert(0, str(result))


def subtractNumbers():
    """Performs subtraction and updates the display."""
    result = n1 - n2
    display.delete(0, tk.END)
    display.insert(0, str(result))


def multiplyNumbers():
    """Performs multiplication and updates the display."""
    result = n1 * n2
    display.delete(0, tk.END)
    display.insert(0, str(result))


def divideNumbers():
    """Performs division and updates the display.
    
    Handles division by zero by displaying an error message.
    """
    display.delete(0, tk.END)

    if n2 == 0:
        display.insert(0, "MATH ERROR")  # Display error if dividing by zero
    else:
        result = n1 / n2
        display.insert(0, str(result))


def equal():
    """Evaluates the expression based on the selected operator."""
    global n2
    n2 = int(display.get())  # Get the second number

    if operator == '+':
        addNumbers()
    elif operator == '-':
        subtractNumbers()
    elif operator == '*':
        multiplyNumbers()
    else:
        divideNumbers()


# Button configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for text, row, col in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear)
    elif text in '+-/*':
        btn = tk.Button(root, text=text, padx=20, pady=20, 
                        command=lambda t=text: clearFirstNumber(t))
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, 
                        command=lambda t=text: update_display(t))
    btn.grid(row=row, column=col)


# Run the main loop
if __name__ == "__main__":
    root.mainloop()
