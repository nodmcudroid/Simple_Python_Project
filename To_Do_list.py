import tkinter as tk
from tkinter import messagebox

# App window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("420x600")
root.config(bg="#1e1e2f")

# Fonts & Colors
FONT_MAIN = ("Segoe UI", 14)
BG = "#1e1e2f"
FG = "#ffffff"
BTN_BG = "#5e60ce"
BTN_HOVER = "#4ea8de"
ENTRY_BG = "#2e2e3f"
SELECT_BG = "#3b82f6"

tasks = []

# Hover effect for buttons
def on_enter(e):
    e.widget.config(bg=BTN_HOVER)

def on_leave(e):
    e.widget.config(bg=BTN_BG)

# Functions
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        messagebox.showwarning("Oops!", "Select a task to delete!")

def clear_all():
    listbox.delete(0, tk.END)
    tasks.clear()

# Header
header = tk.Label(root, text="✅ My To-Do List", font=("Segoe UI", 20, "bold"), bg=BG, fg="#fca311")
header.pack(pady=20)

# Entry box
entry = tk.Entry(root, font=FONT_MAIN, bg=ENTRY_BG, fg=FG, insertbackground="white", bd=0, relief=tk.FLAT)
entry.pack(padx=30, pady=10, fill=tk.X, ipady=10)
entry.config(highlightthickness=2, highlightbackground="#5e60ce")

# Buttons
button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add", font=FONT_MAIN, bg=BTN_BG, fg="white", padx=20, pady=10, bd=0, command=add_task)
btn_add.grid(row=0, column=0, padx=5)
btn_add.bind("<Enter>", on_enter)
btn_add.bind("<Leave>", on_leave)

btn_delete = tk.Button(button_frame, text="Delete", font=FONT_MAIN, bg=BTN_BG, fg="white", padx=20, pady=10, bd=0, command=delete_task)
btn_delete.grid(row=0, column=1, padx=5)
btn_delete.bind("<Enter>", on_enter)
btn_delete.bind("<Leave>", on_leave)

btn_clear = tk.Button(button_frame, text="Clear All", font=FONT_MAIN, bg="#e63946", fg="white", padx=20, pady=10, bd=0, command=clear_all)
btn_clear.grid(row=0, column=2, padx=5)
btn_clear.bind("<Enter>", lambda e: btn_clear.config(bg="#d62828"))
btn_clear.bind("<Leave>", lambda e: btn_clear.config(bg="#e63946"))

# Listbox
listbox = tk.Listbox(root, font=FONT_MAIN, bg=ENTRY_BG, fg=FG, selectbackground=SELECT_BG, activestyle="none", bd=0, highlightthickness=0)
listbox.pack(padx=30, pady=20, fill=tk.BOTH, expand=True)

# Run app
root.mainloop()
