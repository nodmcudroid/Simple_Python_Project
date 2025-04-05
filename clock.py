import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")  # Set fixed size
root.resizable(False, False)  # Prevent resizing
root.configure(bg='black')  # Set background color

# Time Label
label = tk.Label(
    root,
    font=('calibri', 48, 'bold'),
    background='black',
    foreground='cyan'
)
label.pack(expand=True)

# Function to update time
def update_time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, update_time)  # Schedule next update in 1 second

# Start the clock
update_time()

# Run the GUI loop
root.mainloop()
