import tkinter as tk
import random
from tkinter import messagebox

# Lists of skateboarding tricks by difficulty
easy_tricks = [
    "Ollie",
    "Kickflip",
    "Heelflip",
    "Pop Shove-it",
    "Backside 180",
    "Frontside 180",
    "Boneless",
    "Boneless 180",
    "No comply 180",
    "Fakie Ollie",
    "Half cab",
    "Frontside Shuv",
    "Backside Shuv"
]

medium_tricks = [
    "Backside Flip",
    "Frontside Flip",
    "360 Flip",
    "Hardflip",
    "Varial Kickflip",
    "Varial Heelflip",
    "Nollie",
    "Switch Ollie",
    "Nollie Kickflip",
    "Nollie Heelflip",
    "Fakie Kickflip",
    "Fakie Heelflip",
    "Switch Pop Shove-it",
    "Nollie Pop Shove-it",
    "Fakie Pop Shove-it",
    "Switch Frontside 180",
    "Nollie Frontside 180",
    "Fakie Frontside 180",
    "Switch Backside 180",
    "Nollie Backside 180",
    "Fakie Backside 180"
]

hard_tricks = [
    "Switch Frontside Flip",
    "Nollie Frontside Flip",
    "Fakie Frontside Flip",
    "Switch Backside Flip",
    "Nollie Backside Flip",
    "Fakie Backside Flip"
    "Switch Kickflip",
    "Switch Heelflip",
    "Switch Hardflip",
    "Nollie Hardflip",
    "Fakie Hardflip",
    "Switch Varial Kickflip",
    "Nollie Varial Kickflip",
    "Fakie Varial Kickflip",
    "Switch Varial Heelflip",
    "Nollie Varial Heelflip",
    "Fakie Varial Heelflip",
    "Switch 360 Flip",
    "Nollie 360 Flip",
    "Fakie 360 Flip",
    "Double Kickflip",
    "Double Heelflip",
    "Triple Kickflip",
    "Quad Kickflip"
]

def show_trick(difficulty):
    global current_trick
    # Choose a random trick from the selected difficulty level
    if difficulty == "Easy":
        current_trick = random.choice(easy_tricks)
    elif difficulty == "Medium":
        current_trick = random.choice(easy_tricks + medium_tricks)
    else:
        current_trick = random.choice(easy_tricks + medium_tricks + hard_tricks)
    trick_label.config(text=current_trick)
    # Show Yes and No buttons
    yes_button.pack()
    no_button.pack()
    # Hide Generate Trick button
    generate_button.pack_forget()

def landed_yes():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    if score == 10:
        messagebox.showinfo("Congratulations!", "Well done! You reached 10 points!")
        if messagebox.askyesno("Close Application", "Do you want to close the application?"):
            root.destroy()
    else:
        yes_button.pack_forget()
        no_button.pack_forget()
        generate_button.pack()

def landed_no():
    yes_button.pack_forget()
    no_button.pack_forget()
    generate_button.pack()

# Create the main window
root = tk.Tk()
root.title("Skateboarding Trick Generator")
root.geometry("400x300")

# Difficulty label
difficulty_label = tk.Label(root, text="Choose difficulty:", font=("Helvetica", 12))
difficulty_label.pack(pady=10)

# Buttons to choose difficulty
def select_difficulty(difficulty):
    global selected_difficulty
    selected_difficulty = difficulty
    show_trick(selected_difficulty)

easy_button = tk.Button(root, text="Easy", command=lambda: select_difficulty("Easy"))
medium_button = tk.Button(root, text="Medium", command=lambda: select_difficulty("Medium"))
hard_button = tk.Button(root, text="Hard", command=lambda: select_difficulty("Hard"))
easy_button.pack()
medium_button.pack()
hard_button.pack()

# Trick label
current_trick = ""
trick_label = tk.Label(root, text=current_trick, font=("Helvetica", 14))
trick_label.pack(pady=20)

# Yes and No buttons
yes_button = tk.Button(root, text="Yes", command=landed_yes)
no_button = tk.Button(root, text="No", command=landed_no)

# Generate Trick button
generate_button = tk.Button(root, text="Generate Trick", command=lambda: show_trick(selected_difficulty))
generate_button.pack()

# Score label
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Helvetica", 12))
score_label.pack(pady=10)

# Run the main event loop
root.mainloop()
