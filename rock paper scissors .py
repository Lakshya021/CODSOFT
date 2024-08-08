import random
import tkinter as tk

def play_game():
    user_choice = user_var.get()
    comp_choice = random.choice(options)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {comp_choice}")

    if user_choice == comp_choice:
        result_label.config(text=result_label.cget("text") + "\nResult: Draw")
    elif user_choice == "rock" and comp_choice == "paper":
        result_label.config(text=result_label.cget("text") + "\nResult: Computer wins")
    elif user_choice == "rock" and comp_choice == "scissor":
        result_label.config(text=result_label.cget("text") + "\nResult: You win")
    elif user_choice == "paper" and comp_choice == "rock":
        result_label.config(text=result_label.cget("text") + "\nResult: You win")
    elif user_choice == "paper" and comp_choice == "scissor":
        result_label.config(text=result_label.cget("text") + "\nResult: Computer wins")
    elif user_choice == "scissor" and comp_choice == "paper":
        result_label.config(text=result_label.cget("text") + "\nResult: You win")
    elif user_choice == "scissor" and comp_choice == "rock":
        result_label.config(text=result_label.cget("text") + "\nResult: Computer wins")
    else:
        result_label.config(text=result_label.cget("text") + "\nInvalid choice")

options = ["rock", "paper", "scissor"]

root = tk.Tk()
root.title("Rock, Paper, Scissors")

user_var = tk.StringVar(value="rock")

user_label = tk.Label(root, text="Your choice:")
user_label.pack()

user_choice_button = tk.OptionMenu(root, user_var, *options)
user_choice_button.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
