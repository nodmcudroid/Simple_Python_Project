import tkinter as tk
from tkinter import messagebox

# Tip Calculator Function
def calculate_tip():
    try:
        bill_amount = float(bill_entry.get())
        tip_percent = float(tip_entry.get())
        tip = bill_amount * (tip_percent / 100)
        total = bill_amount + tip
        tip_result.config(text=f"Tip: ${tip:.2f}")
        total_result.config(text=f"Total: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Bill Amount
tk.Label(root, text="Bill Amount ($)", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
bill_entry = tk.Entry(root, font=("Arial", 12))
bill_entry.pack(pady=5)

# Tip Percentage
tk.Label(root, text="Tip Percentage (%)", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
tip_entry = tk.Entry(root, font=("Arial", 12))
tip_entry.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate Tip", font=("Arial", 12), bg="#4CAF50", fg="white", command=calculate_tip).pack(pady=10)

# Result Labels
tip_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
tip_result.pack(pady=5)

total_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
total_result.pack(pady=5)

# Run the application
root.mainloop()
