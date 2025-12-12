import random
import tkinter as tk
from tkinter import messagebox
import os
import sys
import ctypes
from PIL import Image, ImageTk
import threading
import pygame

def resource_path(filename):
    import sys, os
    try:
        base_path = sys._MEIPASS  # for PyInstaller
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)


# Hide terminal window on Windows
if os.name == 'nt':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Initialize sound system
pygame.mixer.init()

# Load sound effects
win_sound = pygame.mixer.Sound(resource_path("win.wav"))
lose_sound = pygame.mixer.Sound(resource_path("lose.wav"))
draw_sound = pygame.mixer.Sound(resource_path("draw.wav"))
background_music = resource_path("bg_rps.mp3")

# Set default volumes
pygame.mixer.music.set_volume(0.5)  # 50%
win_sound.set_volume(0.5)            # 50%
lose_sound.set_volume(0.5)
draw_sound.set_volume(0.5)

# Play background music in a separate thread
def play_music():
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)

music_thread = threading.Thread(target=play_music)
music_thread.daemon = True
music_thread.start()

# Value mappings
dict = {"r": -1, "p": 0, "s": 1}
reversedict = {-1: "ROCK", 0: "PAPER", 1: "SCISSOR"}

# Score tracking
score = {"win": 0, "lose": 0, "draw": 0}

# GUI version
def gui_game():
    def play(user_choice):
        user = moves[user_choice]
        computer = random.choice([-1, 0, 1])

        user_label.config(text=f"You: {reverse_moves[user]}")
        comp_label.config(text=f"Computer: {reverse_moves[computer]}")

        user_image_label.config(image=player_images[user_choice])
        comp_image_label.config(image=computer_images[reverse_moves[computer].lower()])

        if user == computer:
            result_label.config(text="Draw 🤝", fg="blue")
            score["draw"] += 1
            draw_sound.play()
        elif (computer == -1 and user == 0) or (computer == 0 and user == 1) or (computer == 1 and user == -1):
            result_label.config(text="You Win ✅", fg="green")
            score["win"] += 1
            win_sound.play()
        else:
            result_label.config(text="You Lose ❌", fg="red")
            score["lose"] += 1
            lose_sound.play()

        update_score()

    def update_score():
        score_label.config(text=f"Wins: {score['win']} | Losses: {score['lose']} | Draws: {score['draw']}")

    def reset_game():
        score["win"] = score["lose"] = score["draw"] = 0
        update_score()
        result_label.config(text="Let's Play!", fg="black")
        user_label.config(text="You:")
        comp_label.config(text="Computer:")
        user_image_label.config(image="")
        comp_image_label.config(image="")

    def update_music_volume(val):
        pygame.mixer.music.set_volume(float(val) / 100)

    def update_effects_volume(val):
        vol = float(val) / 100
        win_sound.set_volume(vol)
        lose_sound.set_volume(vol)
        draw_sound.set_volume(vol)

    gui = tk.Tk()
    gui.title("Rock Paper Scissors")
    gui.iconbitmap(resource_path("rps.ico"))  # sets icon for the window
    gui.geometry("650x800")
    gui.resizable(False, False)

    moves = {"rock": -1, "paper": 0, "scissor": 1}
    reverse_moves = {-1: "ROCK", 0: "PAPER", 1: "SCISSOR"}

    tk.Label(gui, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)

    global user_label, comp_label, result_label, score_label

    label_frame = tk.Frame(gui)
    label_frame.pack(pady=5)

    comp_label = tk.Label(label_frame, text="Computer:", font=("Arial", 12))
    comp_label.pack(side="left", padx=50)

    user_label = tk.Label(label_frame, text="You:", font=("Arial", 12))
    user_label.pack(side="right", padx=50)

    image_frame = tk.Frame(gui)
    image_frame.pack(pady=10)

    comp_image_label = tk.Label(image_frame)
    comp_image_label.pack(side="left", padx=20)

    user_image_label = tk.Label(image_frame)
    user_image_label.pack(side="right", padx=20)

    result_label = tk.Label(gui, text="Let's Play!", font=("Arial", 14))
    result_label.pack(pady=5)

    button_frame = tk.Frame(gui)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("scissor")).pack(side="left", padx=5)

    score_label = tk.Label(gui, text="Wins: 0 | Losses: 0 | Draws: 0", font=("Arial", 12, "bold"))
    score_label.pack(pady=10)

    tk.Button(gui, text="Reset Score", command=reset_game).pack()

    # Volume Sliders
    tk.Label(gui, text="Music Volume", font=("Arial", 10)).pack()
    music_slider = tk.Scale(gui, from_=0, to=100, orient="horizontal", command=update_music_volume)
    music_slider.set(50)
    music_slider.pack()

    tk.Label(gui, text="Sound Effects Volume", font=("Arial", 10)).pack()
    effects_slider = tk.Scale(gui, from_=0, to=100, orient="horizontal", command=update_effects_volume)
    effects_slider.set(50)
    effects_slider.pack()

    # Load PNGs
    player_images = {
        "rock": ImageTk.PhotoImage(Image.open(resource_path("player_rock.png"))),
        "paper": ImageTk.PhotoImage(Image.open(resource_path("player_paper.png"))),
        "scissor": ImageTk.PhotoImage(Image.open(resource_path("player_scissor.png")))
    }

    computer_images = {
        "rock": ImageTk.PhotoImage(Image.open(resource_path("computer_rock.png"))),
        "paper": ImageTk.PhotoImage(Image.open(resource_path("computer_paper.png"))),
        "scissor": ImageTk.PhotoImage(Image.open(resource_path("computer_scissor.png")))
    }

    gui.mainloop()

# Start with GUI
gui_game()
