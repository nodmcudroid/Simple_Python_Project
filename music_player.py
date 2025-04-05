import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load music file
def load_music():
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        status_label.config(text="Loaded: " + file.split("/")[-1])

# Play music
def play_music():
    pygame.mixer.music.play()
    status_label.config(text="Playing...")

# Pause music
def pause_music():
    pygame.mixer.music.pause()
    status_label.config(text="Paused")

# Resume music
def resume_music():
    pygame.mixer.music.unpause()
    status_label.config(text="Resumed")

# Stop music
def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

# Create window
root = tk.Tk()
root.title("Python Music Player")
root.geometry("300x300")
root.config(bg="black")

# Status label
status_label = tk.Label(root, text="Welcome!", bg="black", fg="white")
status_label.pack(pady=10)

# Buttons
tk.Button(root, text="Load Music", command=load_music, width=25).pack(pady=5)
tk.Button(root, text="Play", command=play_music, width=25).pack(pady=5)
tk.Button(root, text="Pause", command=pause_music, width=25).pack(pady=5)
tk.Button(root, text="Resume", command=resume_music, width=25).pack(pady=5)
tk.Button(root, text="Stop", command=stop_music, width=25).pack(pady=5)

# Run the GUI
root.mainloop()
