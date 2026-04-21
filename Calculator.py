########### 627960
########## Subaita Sajjad
######### 12/10/24
########## Calculator
######## Made a working Calculator.

import tkinter as tk  

def click(event):
    button_text = event.widget.cget("text")
    
    # If "=" is clicked, find the result
    if button_text == "=":
        try:
            # Use eval to calculate the result from the entry field
            result = eval(entry.get())
            entry.delete(0, tk.END) 
            entry.insert(tk.END, result) 
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    
    elif button_text == "C":
        entry.delete(0, tk.END)
    
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field for displaying input and output
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)  # Place the entry field
root.configure(bg="white")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Loop through the button layout and create buttons
for row_index, row in enumerate(buttons): 
    for col_index, button_text in enumerate(row):  

        # Create a button with the text
        button = tk.Button(root, text=button_text, font=("Arial", 15), width=5, height=2, bg="lightpink")
        button.grid(row=row_index + 1, column=col_index, padx=5, pady=5) 
        button.bind("<Button-1>", click)  

root.mainloop()
