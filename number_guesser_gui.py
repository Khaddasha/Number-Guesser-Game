import tkinter as tk
from tkinter import messagebox
import random

class NumberGuesserGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guesser Game")

        self.random_num = None

        self.start_label = tk.Label(master, text="Enter the start of the range:")
        self.start_label.pack()
        self.start_entry = tk.Entry(master)
        self.start_entry.pack()

        self.end_label = tk.Label(master, text="Enter the end of the range:")
        self.end_label.pack()
        self.end_entry = tk.Entry(master)
        self.end_entry.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())

            if start >= end:
                messagebox.showerror("Error", "End value should be greater than start value.")
            else:
                self.random_num = random.randint(start, end)
                messagebox.showinfo("Game Started", "I've chosen a number. Start guessing!")

                guess_label = tk.Label(self.master, text="Enter your guess:")
                guess_label.pack()

                self.guess_entry = tk.Entry(self.master)
                self.guess_entry.pack()

                submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
                submit_button.pack()

                self.start_button.config(state=tk.DISABLED)  # Disable the "Start Game" button after starting the game

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for the range.")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess == self.random_num:
                messagebox.showinfo("Congratulations!", "You guessed the correct number!")
                self.master.destroy()
            elif guess < self.random_num:
                messagebox.showinfo("Try again", "Too low! Try a higher number.")
            else:
                messagebox.showinfo("Try again", "Too high! Try a lower number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuesserGame(root)
    root.mainloop()
