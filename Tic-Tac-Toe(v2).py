import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x330")
root.resizable(False, False)

# Global variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    # Check for draw
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Draw"
    
    return None

def on_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

# UI setup
frame = tk.Frame(root)
frame.pack(pady=10)

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=5)

root.mainloop()
