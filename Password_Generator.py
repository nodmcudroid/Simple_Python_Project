import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())

    characters = ""
    if use_upper.get():
        characters += string.ascii_uppercase
    if use_lower.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character set!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# Variables
password_var = tk.StringVar()
length_entry = tk.Entry(root, width=5)
length_entry.insert(0, "12")
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

# Layout
tk.Label(root, text="Password Length:", fg="white", bg="#1e1e2e").pack(pady=5)
length_entry.pack()

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper, fg="white", bg="#1e1e2e", selectcolor="#333").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase", variable=use_lower, fg="white", bg="#1e1e2e", selectcolor="#333").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Digits", variable=use_digits, fg="white", bg="#1e1e2e", selectcolor="#333").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, fg="white", bg="#1e1e2e", selectcolor="#333").pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4f46e5", fg="white", padx=10, pady=5).pack(pady=10)
tk.Entry(root, textvariable=password_var, width=30, font=("Courier", 12), justify='center').pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#22c55e", fg="white", padx=10, pady=5).pack()

root.mainloop()
