import tkinter as tk
from tkinter import messagebox
import webbrowser
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to perform search
def search_tool():
    query = search_entry.get()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        engine.say(f"Searching for {query}")
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

# Create the main window
root = tk.Tk()
root.title("Search Tool")
root.geometry("500x400")
root.config(bg="#2b2b2b")

# Create a frame for center alignment
frame = tk.Frame(root, bg="#2b2b2b", pady=50)
frame.pack(pady=50)

# Add heading label
heading = tk.Label(frame, text="Search Tool", font=("Monoton", 32, "bold"), fg="white", bg="#2b2b2b")
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Add search entry field
search_entry = tk.Entry(frame, font=("Arial", 14), width=30, bg="#333333", fg="white", bd=2, relief="flat")
search_entry.grid(row=1, column=0, columnspan=2, pady=10)

# Add search button
search_button = tk.Button(frame, text="Search", font=("Arial", 14, "bold"), bg="#FF4081", fg="white", command=search_tool)
search_button.grid(row=2, column=0, columnspan=2, pady=20)

# Add radio buttons for search engine choice (Google, Bing, Yahoo)
radio_var = tk.StringVar(value="Google")
radio_google = tk.Radiobutton(frame, text="Google", font=("Arial", 12), value="Google", variable=radio_var, bg="#2b2b2b", fg="white", selectcolor="#FF4081")
radio_bing = tk.Radiobutton(frame, text="Bing", font=("Arial", 12), value="Bing", variable=radio_var, bg="#2b2b2b", fg="white", selectcolor="#FF4081")
radio_yahoo = tk.Radiobutton(frame, text="Yahoo", font=("Arial", 12), value="Yahoo", variable=radio_var, bg="#2b2b2b", fg="white", selectcolor="#FF4081")

radio_google.grid(row=3, column=0, padx=10, pady=5)
radio_bing.grid(row=3, column=1, padx=10, pady=5)
radio_yahoo.grid(row=4, column=0, columnspan=2, pady=5)

# Main loop
root.mainloop()
