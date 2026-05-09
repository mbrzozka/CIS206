# Data Entry/Calculation Form using Tkinter
# This program creates a basic GUI form that prompts the user to enter a string (their name) 
# and a number. When the button is clicked, the program validates the numeric input, performs
# a simple calculation, and displays the result on the form.

import tkinter as tk
from tkinter import messagebox

# Function that runs when button is clicked
def process_input():
    # Get the text from the entry boxes
    name = name_entry.get()
    number_text = number_entry.get()
    # Validate that the number box contains a numeric value
    if not number_text.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return
    # Convert the numeric text to an integer
    number = int(number_text)
    # Perform a simple calculation (double the number)
    result = number * 2
    # Display the output in the label
    output_label.config(text=f"Hello {name}, your number doubled is: {result}")

# Build the main form window
window = tk.Tk()
window.title("Data Entry/Calculation Form")
window.geometry("400x250")
# Label + text box for name (string input)
tk.Label(window, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(window, width=30)
name_entry.pack()
# Label + text box for number (numeric input)
tk.Label(window, text="Enter a number:").pack(pady=5)
number_entry = tk.Entry(window, width=30)
number_entry.pack()
# Button that triggers the calculation
calc_button = tk.Button(window, text="Process Input", command=process_input)
calc_button.pack(pady=15)
# Output label (shows results)
output_label = tk.Label(window, text="", font=("Arial", 12))
output_label.pack(pady=10)
# Start the Tkinter loop
window.mainloop()