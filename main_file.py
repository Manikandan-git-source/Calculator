import tkinter as tk  # importing the tkinter.

calculation = ""  # global variable to access and modify it through these functions.


def add_to_calculation(symbol):  # symbol denotes the numbers, operators and parenthesis.
    global calculation
    calculation += str(symbol)  # Type casting because 'str' does not concatenate with the 'int'.
    text_result.delete(1.0, "end")  # deleting the previous math expression to avoid the confusion to user.
    text_result.insert(1.0, calculation)  # inserting the result.


def evaluate_calculation():
    global calculation
    try:  # try-except block is used to prevent the program from crashing if the bug occurs.
        calculation = str(eval(calculation))  # evaluate the string expressions.
        text_result.delete(1.0, "end")  # delete the whole thing from the text field widget.
        text_result.insert(1.0, calculation)  # we are going to insert the calculation.
    except Exception:
        clear_field()
        text_result.insert(1.0, "Error")  # eg: Syntax Error or Zero Division Error.


def clear_field():  # this function will clear the fields if user might want to clear.
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()  # Creating the root object for the main window in tkinter.
root.geometry("300x275")  # create the calculator window size.

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)  # create 5 columns in the grid.

btn_1 = tk.Button(root, text=1, command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text=2, command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text=3, command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text=4, command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text=5, command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text=6, command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text=7, command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text=8, command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text=9, command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text=0, command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_multiplication = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiplication.grid(row=4, column=4)

btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_division.grid(row=5, column=4)

btn_open_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open_parenthesis.grid(row=5, column=1)

btn_close_parenthesis = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close_parenthesis.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))  # this is the button.
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equal_to = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))  # the button.
btn_equal_to.grid(row=6, column=3, columnspan=4)

root.mainloop()  # Running the mainloop , because it will halt the window until the user closes it manually.
