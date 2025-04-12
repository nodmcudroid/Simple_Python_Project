import tkinter as tk
from tkinter import ttk
import time
import random

# Sample text
TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed measures how fast you can type words.",
    "Practice every day to improve your typing skills.",
    "Python is a versatile language used in many fields.",
    "Focus on accuracy before increasing your typing speed."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x500")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.text_to_type = random.choice(TEXTS)
        self.start_time = None

        # Title
        self.title_label = tk.Label(
            root, text="Typing Speed Test", font=("Helvetica", 28, "bold"),
            fg="white", bg="#1a1a2e"
        )
        self.title_label.pack(pady=(30, 10))

        # Radiobutton frame
        self.mode_frame = tk.Frame(root, bg="#1a1a2e")
        self.mode_frame.pack(pady=10)

        self.mode = tk.StringVar(value="easy")
        self.create_radiobutton("Easy", "easy")
        self.create_radiobutton("Medium", "medium")
        self.create_radiobutton("Hard", "hard")

        # Display text to type
        self.text_display = tk.Label(
            root, text=self.text_to_type, wraplength=700, justify="center",
            font=("Helvetica", 14), fg="white", bg="#1a1a2e", padx=20, pady=10
        )
        self.text_display.pack(pady=20)

        # Entry box
        self.entry = tk.Text(root, height=5, width=80, font=("Helvetica", 12), wrap="word")
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)

        # Button
        self.check_button = tk.Button(
            root, text="Check Speed", font=("Helvetica", 14, "bold"),
            bg="#00adb5", fg="white", activebackground="#393e46", activeforeground="white",
            command=self.check_speed, padx=10, pady=5
        )
        self.check_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"),
                                     fg="#00ffcc", bg="#1a1a2e")
        self.result_label.pack(pady=10)

    def create_radiobutton(self, text, value):
        rb = tk.Radiobutton(
            self.mode_frame, text=text, variable=self.mode, value=value,
            font=("Helvetica", 12, "bold"), bg="#1a1a2e", fg="white",
            activebackground="#1a1a2e", activeforeground="#00adb5",
            selectcolor="#393e46", indicatoron=0, width=10, padx=10, pady=5,
            borderwidth=2, relief="raised"
        )
        rb.pack(side="left", padx=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_speed(self):
        typed_text = self.entry.get("1.0", tk.END).strip()
        end_time = time.time()
        time_taken = end_time - self.start_time if self.start_time else 1

        # Calculate Words Per Minute
        word_count = len(typed_text.split())
        wpm = round((word_count / time_taken) * 60)

        # Accuracy
        correct_chars = sum(1 for a, b in zip(typed_text, self.text_to_type) if a == b)
        accuracy = round((correct_chars / len(self.text_to_type)) * 100)

        self.result_label.config(
            text=f"Speed: {wpm} WPM | Accuracy: {accuracy}%"
        )
        self.start_time = None
        self.entry.delete("1.0", tk.END)

        # New text
        self.text_to_type = random.choice(TEXTS)
        self.text_display.config(text=self.text_to_type)


if __name__ == "__main__":
    root = tk.Tk()
    TypingSpeedTest(root)
    root.mainloop()
