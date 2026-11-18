
import tkinter as tk
import random

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x550")
root.config(bg="#202040")
root.resizable(False, False)

# Score Variables
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Heading
heading = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 22, "bold"),
    bg="#202040",
    fg="white"
)
heading.pack(pady=25)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 15),
    bg="#202040",
    fg="#FFD700"
)
instruction.pack(pady=10)

# Result Display
result_label = tk.Label(
    root,
    text="Let's Play!",
    font=("Arial", 20, "bold"),
    bg="#202040",
    fg="white"
)
result_label.pack(pady=15)

# Computer Choice
computer_label = tk.Label(
    root,
    text="Computer: Waiting...",
    font=("Arial", 14),
    bg="#202040",
    fg="#00FFFF"
)
computer_label.pack(pady=10)

# Score Display
score_label = tk.Label(
    root,
    text="Your Score: 0     Computer Score: 0",
    font=("Arial", 14, "bold"),
    bg="#202040",
    fg="white"
)
score_label.pack(pady=20)

# Game Function
def play(user_choice):

    global user_score, computer_score

    computer_choice = random.choice(choices)

    computer_label.config(
        text="Computer: " + computer_choice
    )

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "Congratulations! You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"

        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}     Computer Score: {computer_score}"
    )

# Buttons Frame
button_frame = tk.Frame(root, bg="#202040")
button_frame.pack(pady=25)

# Rock Button
rock_button = tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 13, "bold"),
    bg="#FF9800",
    fg="white",
    width=10,
    height=2,
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

# Paper Button
paper_button = tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 13, "bold"),
    bg="#2196F3",
    fg="white",
    width=10,
    height=2,
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

# Scissors Button
scissors_button = tk.Button(
    button_frame,
    text="✂ SCISSORS",
    font=("Arial", 12, "bold"),
    bg="#E91E63",
    fg="white",
    width=10,
    height=2,
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

# Reset Function
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    result_label.config(text="Let's Play!")
    computer_label.config(text="Computer: Waiting...")
    score_label.config(
        text="Your Score: 0     Computer Score: 0"
    )

# Reset Button
reset_button = tk.Button(
    root,
    text="RESET GAME",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    command=reset_game
)
reset_button.pack(pady=15)

# Exit Button
exit_button = tk.Button(
    root,
    text="EXIT GAME",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    width=18,
    command=root.destroy
)
exit_button.pack(pady=5)

# Run Game
root.mainloop()
