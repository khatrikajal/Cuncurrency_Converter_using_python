import tkinter as tk
from tkinter import messagebox

# Create the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

# Set the initial player
current_player = "X"

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=" ", width=10, height=5,
                           command=lambda row=row, col=col: on_button_click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)

# Create the function that will run when a button is clicked
def on_button_click(row, col):
    global current_player
    button = buttons[row][col]
    if button["text"] == " ":
        button["text"] = current_player
        if has_won(current_player):
            messagebox.showinfo("Tic Tac Toe", f"{current_player} wins!")
            root.destroy()
        elif is_tie():
            messagebox.showinfo("Tic Tac Toe", "Tie game!")
            root.destroy()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create the function to check if a player has won
def has_won(player):
    for i in range(3):
        # Check rows
        if (buttons[i][0]["text"] == player and
            buttons[i][1]["text"] == player and
            buttons[i][2]["text"] == player):
            return True
        # Check columns
        elif (buttons[0][i]["text"] == player and
              buttons[1][i]["text"] == player and
              buttons[2][i]["text"] == player):
            return True
    # Check diagonals
    if (buttons[0][0]["text"] == player and
        buttons[1][1]["text"] == player and
        buttons[2][2]["text"] == player):
        return True
    elif (buttons[0][2]["text"] == player and
          buttons[1][1]["text"] == player and
          buttons[2][0]["text"] == player):
        return True
    return False

# Create the function to check if the game is a tie
def is_tie():
    for row in buttons:
        for button in row:
            if button["text"] == " ":
                return False
    return True

# Run the GUI
root.mainloop()
