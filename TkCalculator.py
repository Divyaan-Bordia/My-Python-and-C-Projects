import tkinter as tk

# Functions
def add_to_expression(value):
    current_text = entry.get()
    if current_text == "0" and value != ".":
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)
    else:
        entry.insert(tk.END, value)

def clear_entry(event=None):
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

def toggle_sign():
    current_text = entry.get()
    if current_text.startswith("-"):
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[1:])
    else:
        if current_text != "0":
            entry.delete(0, tk.END)
            entry.insert(tk.END, "-" + current_text)

def calculate_percent():
    try:
        current_value = float(entry.get())
        percent_value = current_value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(percent_value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def evaluate_expression(event=None):
    try:
        expression = entry.get().replace("x", "*")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def backspace(event=None):
    current_text = entry.get()
    if len(current_text) > 1:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    else:
        clear_entry()

def key_pressed(event):
    char = event.char
    if char in "0123456789.+-/*":
        add_to_expression(char)
    elif char == "x":
        add_to_expression("*")
    elif char == "=" or event.keysym == "Return":
        evaluate_expression()
    elif char.upper() == "C":
        clear_entry()
    elif event.keysym == "BackSpace":
        backspace()

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="black")

# Entry
entry = tk.Entry(root, font=("Arial", 36), bg="black", fg="white", borderwidth=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=20)
entry.insert(0, "0")

# Button details
button_font = ("Arial", 24)
button_bg = {
    "number": "grey",
    "operator": "orange",
    "function": "lightgrey"
}

# Layout
buttons = [
    ("C", 1, 0, clear_entry, "function"),
    ("+/-", 1, 1, toggle_sign, "function"),
    ("%", 1, 2, calculate_percent, "function"),
    ("/", 1, 3, lambda: add_to_expression("/"), "operator"),

    ("7", 2, 0, lambda: add_to_expression("7"), "number"),
    ("8", 2, 1, lambda: add_to_expression("8"), "number"),
    ("9", 2, 2, lambda: add_to_expression("9"), "number"),
    ("*", 2, 3, lambda: add_to_expression("*"), "operator"),

    ("4", 3, 0, lambda: add_to_expression("4"), "number"),
    ("5", 3, 1, lambda: add_to_expression("5"), "number"),
    ("6", 3, 2, lambda: add_to_expression("6"), "number"),
    ("-", 3, 3, lambda: add_to_expression("-"), "operator"),

    ("1", 4, 0, lambda: add_to_expression("1"), "number"),
    ("2", 4, 1, lambda: add_to_expression("2"), "number"),
    ("3", 4, 2, lambda: add_to_expression("3"), "number"),
    ("+", 4, 3, lambda: add_to_expression("+"), "operator"),

    ("0", 5, 0, lambda: add_to_expression("0"), "number"),
    (".", 5, 2, lambda: add_to_expression("."), "number"),
    ("=", 5, 3, evaluate_expression, "operator"),
]

# Create buttons
for (text, row, col, command, category) in buttons:
    btn_color = button_bg[category]
    btn = tk.Button(
        root,
        text=text,
        command=command,
        font=button_font,
        bg=btn_color,
        fg="white",
        activebackground=btn_color,
        activeforeground="white",
        borderwidth=0
    )
    if text == "0":
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
    else:
        btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Row and column sizing
for i in range(6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

# Key binding
root.bind("<Key>", key_pressed)

root.mainloop()
