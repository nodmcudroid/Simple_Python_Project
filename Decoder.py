import tkinter as tk
from tkinter import ttk

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode='encode'):
    result = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            shift = shift if mode == 'encode' else -shift
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# GUI functions
def encode_text():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_value.get())
    result = caesar_cipher(text, shift, mode='encode')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

def decode_text():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_value.get())
    result = caesar_cipher(text, shift, mode='decode')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")
root.geometry("500x500")
root.config(bg="#1e1e1e")

# Add a gradient background effect
def gradient_bg(canvas):
    canvas.create_rectangle(0, 0, 500, 500, fill="#2C3E50", outline="")
    canvas.create_rectangle(0, 0, 500, 500, fill="#34495E", outline="")
    canvas.create_rectangle(0, 0, 500, 500, fill="#1abc9c", outline="")

# Header Label
header_label = tk.Label(root, text="Caesar Cipher", font=("Monoton", 30), fg="white", bg="#1e1e1e")
header_label.pack(pady=20)

# Input Text Area
input_label = tk.Label(root, text="Enter Text:", font=("Arial", 14), fg="white", bg="#1e1e1e")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=50, font=("Arial", 12), fg="black", bg="#ecf0f1", bd=0, relief="flat")
input_text.pack(pady=10)

# Shift Value Label and Entry
shift_label = tk.Label(root, text="Enter Shift Value:", font=("Arial", 14), fg="white", bg="#1e1e1e")
shift_label.pack(pady=5)
shift_value = tk.Entry(root, font=("Arial", 12), fg="black", bg="#ecf0f1", bd=0)
shift_value.pack(pady=10)

# Encoding and Decoding Buttons with modern style
encode_button = tk.Button(root, text="Encode", font=("Arial", 14, "bold"), fg="white", bg="#1abc9c", 
                          relief="flat", command=encode_text)
encode_button.pack(pady=15, fill="x", padx=50)

decode_button = tk.Button(root, text="Decode", font=("Arial", 14, "bold"), fg="white", bg="#e74c3c", 
                          relief="flat", command=decode_text)
decode_button.pack(pady=15, fill="x", padx=50)

# Output Text Area
output_label = tk.Label(root, text="Output:", font=("Arial", 14), fg="white", bg="#1e1e1e")
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=50, font=("Arial", 12), fg="black", bg="#ecf0f1", bd=0, relief="flat")
output_text.pack(pady=10)

# Radiobuttons for Encoder/Decoder
mode_var = tk.StringVar(value='encode')
encode_rb = tk.Radiobutton(root, text="Encode", variable=mode_var, value="encode", font=("Arial", 12), 
                           fg="white", bg="#1e1e1e", selectcolor="#1abc9c", relief="flat")
encode_rb.pack(pady=5)

decode_rb = tk.Radiobutton(root, text="Decode", variable=mode_var, value="decode", font=("Arial", 12), 
                           fg="white", bg="#1e1e1e", selectcolor="#e74c3c", relief="flat")
decode_rb.pack(pady=5)

# Run the application
root.mainloop()
