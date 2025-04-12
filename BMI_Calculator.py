import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            result = f"Underweight: {bmi:.2f}"
        elif 18.5 <= bmi < 24.9:
            result = f"Normal weight: {bmi:.2f}"
        elif 25 <= bmi < 29.9:
            result = f"Overweight: {bmi:.2f}"
        else:
            result = f"Obese: {bmi:.2f}"

        result_label.config(text=result)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#2C3E50")

# Title label
title_label = tk.Label(root, text="BMI Calculator", font=("Monoton", 24, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=20)

# Weight input
weight_label = tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50")
weight_label.pack(pady=10)

weight_entry = tk.Entry(root, font=("Arial", 14), width=20)
weight_entry.pack(pady=5)

# Height input
height_label = tk.Label(root, text="Enter Height (m):", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50")
height_label.pack(pady=10)

height_entry = tk.Entry(root, font=("Arial", 14), width=20)
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14, "bold"), fg="white", bg="#E74C3C", command=calculate_bmi)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#2C3E50")
result_label.pack(pady=20)

# Run the application
root.mainloop()
