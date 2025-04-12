import tkinter as tk
from tkinter import ttk

# Conversion factors relative to meters
conversion_factors = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
}

# Function to convert units
def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        # Convert to base (meter), then to target
        value_in_meters = value * conversion_factors[from_unit]
        result = value_in_meters / conversion_factors[to_unit]
        label_result.config(text=f"{result:.4f} {to_unit}")
    except ValueError:
        label_result.config(text="Please enter a valid number")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")
root.resizable(False, False)

# Title
tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Entry for value
entry_value = tk.Entry(root, width=20, font=("Arial", 12))
entry_value.pack(pady=5)

# Dropdowns for units
unit_list = list(conversion_factors.keys())

combo_from = ttk.Combobox(root, values=unit_list, font=("Arial", 12), state="readonly")
combo_from.set("Meter")
combo_from.pack(pady=5)

combo_to = ttk.Combobox(root, values=unit_list, font=("Arial", 12), state="readonly")
combo_to.set("Kilometer")
combo_to.pack(pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 12), command=convert)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=5)

# Run app
root.mainloop()
