# Smart_Utility_Bill_Estimator 

1. Importing Required Modules
import tkinter as tk
from tkinter import ttk, messagebox

tkinter is Python’s built-in module for GUI development.
ttk provides themed widgets (better-looking buttons, labels, etc.).
messagebox allows us to show pop-up error messages.

2. Bill Estimation Logic
def estimate_bill(utility, amount):
This function takes two arguments:

utility – selected utility type ("Electricity", "Water", "Gas")

amount – the consumption amount entered by the user

    match utility:
Here, we use the Python 3.10+ match statement to select the logic block depending on the value of utility.

        case "Electricity":
If utility is "Electricity":

        if amount <= 100:
                return amount * 5
First 100 units cost ₹5 per unit.


            elif amount <= 300:
                return (100 * 5) + (amount - 100) * 7
Next 200 units cost ₹7 per unit.

            else:
                return (100 * 5) + (200 * 7) + (amount - 300) * 10
Anything above 300 costs ₹10 per unit.

Water and Gas cases follow similar patterns:

        case "Water":
            if amount <= 1000:
                return amount * 0.01
            elif amount <= 5000:
                return (1000 * 0.01) + (amount - 1000) * 0.015
            else:
                return (1000 * 0.01) + (4000 * 0.015) + (amount - 5000) * 0.02

        case "Gas":
            return 50 + amount * 8
Flat ₹50 base charge, plus ₹8 per cubic meter.

        case _:
            return None
Wildcard case: returns None for invalid input.

3. Function to Handle Button Click
def calculate():
Triggered when the user clicks the "Estimate Bill" button.

    utility = utility_var.get()
Gets selected utility type from the dropdown.

    try:
        amount = float(amount_entry.get())
Tries to read and convert user input to a float.

        if amount < 0:
            raise ValueError("Negative input")
Prevents negative values.

        bill = estimate_bill(utility, amount)
Calls the earlier function to calculate the bill.

        result_label.config(text=f"Estimated {utility} Bill: ₹{bill:.2f}")
Updates the label on the screen with formatted bill result.

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive number.")
If input can't be converted to float or is invalid, show a popup.

4. Main GUI Window
root = tk.Tk()
root.title("Utility Bill Estimator")
root.geometry("350x250")
root.resizable(False, False)
Creates the main window.
Sets the title, size, and disables resizing.

5. Dropdown for Utility Type
utility_var = tk.StringVar(value="Electricity")
Stores the selected option.

ttk.Label(root, text="Select Utility:", font=("Arial", 12)).pack(pady=5)
Creates a label for the dropdown.

utility_menu = ttk.Combobox(root, textvariable=utility_var, values=["Electricity", "Water", "Gas"], state="readonly")
utility_menu.pack(pady=5)
Creates a dropdown (combobox) with 3 options. readonly disables manual entry.

6. Entry for Amount
ttk.Label(root, text="Enter Usage:", font=("Arial", 12)).pack(pady=5)
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)
Adds label and entry box for the user to input consumption.

7. Button to Trigger Calculation
ttk.Button(root, text="Estimate Bill", command=calculate).pack(pady=10)
Creates a button that calls calculate() when clicked.

8. Label to Show Result
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)
An empty label that updates to show the estimated bill after clicking the button.

9. Start the GUI Event Loop
root.mainloop()
This keeps the GUI running, waiting for user interaction.

OVERLOOK OF OUTPUT:
![Screenshot (7)](https://github.com/user-attachments/assets/dc31d2b3-88eb-46cd-8450-c970064f95f2)

![Screenshot (8)](https://github.com/user-attachments/assets/a540d83c-0f70-4af0-afc5-17388cbd0e0b)

![Screenshot (9)](https://github.com/user-attachments/assets/fe6d903e-895a-47f7-ae97-9d23b2a350fb)

