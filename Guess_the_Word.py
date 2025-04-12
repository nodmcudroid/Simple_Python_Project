import tkinter as tk
from tkinter import messagebox
import random

# Word list for the game
words = ['python', 'hangman', 'challenge', 'programming', 'interface', 'keyboard', 'development']

# Pick a random word
word = random.choice(words)
guessed = ['_'] * len(word)
attempts_left = 6
guessed_letters = set()

# Function to update display
def update_display():
    word_display.set(' '.join(guessed))
    attempts_display.set(f"Attempts Left: {attempts_left}")
    letters_display.set("Guessed Letters: " + ', '.join(sorted(guessed_letters)))

# Function to process the guess
def guess_letter():
    global attempts_left
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
        return

    guessed_letters.add(letter)

    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                guessed[idx] = letter
    else:
        attempts_left -= 1

    update_display()

    if '_' not in guessed:
        messagebox.showinfo("You Win!", f"Congratulations! The word was '{word}'.")
        root.destroy()
    elif attempts_left == 0:
        messagebox.showinfo("Game Over", f"You ran out of attempts. The word was '{word}'.")
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Guess the Word")
root.geometry("400x300")
root.resizable(False, False)

word_display = tk.StringVar()
attempts_display = tk.StringVar()
letters_display = tk.StringVar()

update_display()

tk.Label(root, text="Guess the Word", font=("Helvetica", 20, "bold")).pack(pady=10)
tk.Label(root, textvariable=word_display, font=("Consolas", 24)).pack(pady=10)
tk.Label(root, textvariable=attempts_display, font=("Helvetica", 14)).pack(pady=5)
tk.Label(root, textvariable=letters_display, font=("Helvetica", 12)).pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 18), width=5, justify="center")
entry.pack(pady=10)

tk.Button(root, text="Guess", font=("Helvetica", 14), command=guess_letter).pack()

root.mainloop()
