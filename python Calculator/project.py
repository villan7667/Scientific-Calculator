import tkinter as tk
from tkinter import messagebox


def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def button_click(symbol):
    entry.insert(tk.END, symbol)


def clear_entry():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Scientific Calculator HSGF")


entry = tk.Entry(root, width=40, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=10, height=2, font=('Arial', 14),
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)


tk.Button(root, text='C', width=10, height=2, font=('Arial', 14), command=clear_entry).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text='(', width=10, height=2, font=('Arial', 14), command=lambda: button_click('(')).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text=')', width=10, height=2, font=('Arial', 14), command=lambda: button_click(')')).grid(row=5, column=2, padx=5, pady=5)


tk.Button(root, text='sin', width=10, height=2, font=('Arial', 14), command=lambda: button_click('sin(')).grid(row=1, column=4, padx=5, pady=5)
tk.Button(root, text='cos', width=10, height=2, font=('Arial', 14), command=lambda: button_click('cos(')).grid(row=2, column=4, padx=5, pady=5)
tk.Button(root, text='tan', width=10, height=2, font=('Arial', 14), command=lambda: button_click('tan(')).grid(row=3, column=4, padx=5, pady=5)
tk.Button(root, text='^', width=10, height=2, font=('Arial', 14), command=lambda: button_click('**')).grid(row=4, column=4, padx=5, pady=5)


root.bind('<Return>', lambda event=None: evaluate_expression())


root.mainloop()
