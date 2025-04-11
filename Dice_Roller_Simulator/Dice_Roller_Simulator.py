import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random

class DiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Roller Simulator")
        self.root.geometry("300x350")
        self.root.configure(bg="#222222")

        # Load dice face images (1 to 6)
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"dice{i}.png").resize((100, 100)))
            for i in range(1, 7)
        ]

        # Load rolling dice GIF frames
        self.roll_gif = []
        gif = Image.open("dice_roll.gif")
        try:
            while True:
                frame = gif.copy().resize((100, 100))
                self.roll_gif.append(ImageTk.PhotoImage(frame.convert("RGBA")))
                gif.seek(len(self.roll_gif))
        except EOFError:
            pass

        self.dice_label = Label(self.root, image=self.dice_images[0], bg="#222222")
        self.dice_label.pack(pady=20)

        self.roll_button = Button(
            self.root, text="Roll Dice", command=self.start_roll,
            font=("Arial", 14, "bold"), bg="#FF3366", fg="white", relief="raised", bd=4
        )
        self.roll_button.pack(pady=10)

        self.result_label = Label(self.root, text="", font=("Arial", 14),
                                  bg="#222222", fg="white")
        self.result_label.pack(pady=10)

        self.frame_index = 0
        self.is_animating = False

    def start_roll(self):
        if not self.is_animating:
            self.frame_index = 0
            self.is_animating = True
            self.result_label.config(text="")
            self.animate_gif()

    def animate_gif(self):
        if self.frame_index < len(self.roll_gif):
            self.dice_label.configure(image=self.roll_gif[self.frame_index])
            self.frame_index += 1
            self.root.after(50, self.animate_gif)
        else:
            self.show_result()

    def show_result(self):
        result = random.randint(1, 6)
        self.dice_label.configure(image=self.dice_images[result - 1])
        self.result_label.config(text=f"You rolled a {result}!")
        self.is_animating = False

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRoller(root)
    root.mainloop()
