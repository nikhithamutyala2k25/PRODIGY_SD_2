import random
import tkinter as tk

def new_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    label.config(text="Enter your guess:", fg="red", bg="white", font=("Arial", 20))
    entry.delete(0, "end")
    result_label.config(text="", fg="green", bg="white", font=("Arial", 20))
    attempts_label.config(text="Attempts: 0", fg="red", bg="white", font=("Arial", 20))
    game_elements.pack()

def check_guess():
    global attempts
    guess = int(entry.get())
    entry.delete(0, "end")

    if guess < number:
        result_label.config(text="Guess higher!", font=("Arial", 20), fg="red", bg="white")
    elif guess > number:
        result_label.config(text="Guess lower!", font=("Arial", 20), fg="red", bg="white")
    else:
        result_label.config(text="YOU WON!", font=("Arial", 20), fg="red", bg="white")

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}", font=("Arial", 20), fg="red", bg="white")

root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="black")
root.geometry("700x700")

number = 0
attempts = 0

game_elements = tk.Frame(root, bg="black")
game_elements.pack(pady=20)

label = tk.Label(game_elements, text="Enter your guess", fg="red", bg="white", font=("Arial", 20))
label.pack(pady=10)

entry = tk.Entry(game_elements)
entry.pack(pady=10)

check_button = tk.Button(game_elements, text="Check", command=check_guess, fg="white", bg="green", font=("Arial", 16))
check_button.pack(pady=10)

result_label = tk.Label(game_elements, text="", fg="green", bg="white", font=("Arial", 20))
result_label.pack(pady=10)

attempts_label = tk.Label(game_elements, text="Attempts: 0", fg="red", bg="white", font=("Arial", 20))
attempts_label.pack(pady=10)

new_game()

root.mainloop()
