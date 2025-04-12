import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (2 Player)")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_gui()

    def create_gui(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('Helvetica', 32), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="Restart", font=('Helvetica', 14),
                                      command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
                (0,3,6), (1,4,7), (2,5,8),  # columns
                (0,4,8), (2,4,6)]           # diagonals
        for i, j, k in wins:
            if b[i] == b[j] == b[k] and b[i] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
