import tkinter as tk
from tkinter import font

def add_digit(digit):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(digit))
    calculate()

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

def square():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, "(" + current_text + ")**2")
    calculate()

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

def add_decimal():
    current_text = entry.get()
    if "." not in current_text:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + ".")

root = tk.Tk()
root.title("Калькулятор")

entry_font = font.Font(family="Segoe UI", size=12, weight="bold")

result_label = tk.Label(root, text="Result:", font=("Segoe UI", 12), bg="#F3F3F3")
result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

entry = tk.Entry(root, font=entry_font, bg="#F3F3F3", justify="right")
entry.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

buttons = [
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
    ("0", 5, 1),
    ("+", 2, 3), ("-", 3, 3), ("*", 4, 3), ("/", 5, 3),
    ("=", 5, 2), ("^2", 5, 0), ("C", 5, 0), (".", 5, 1), ("%", 1, 0)
]

for (text, row, column) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=calculate, bg="#005A9E", fg="white")
    elif text == "^2":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=square, bg="#F3F3F3")
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=clear, bg="#F3F3F3")
    elif text == ".":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=add_decimal, bg="#F3F3F3")
    elif text == "%":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=lambda t=text: add_digit(t), bg="#F3F3F3")
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Segoe UI", 12, "bold"), command=lambda t=text: add_digit(t), bg="#F3F3F3")
    button.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()



