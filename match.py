import tkinter as tk
from tkinter import ttk, messagebox

# ----- Bill Estimation Logic -----
def estimate_bill(utility, amount):
    match utility:
        case "Electricity":
            if amount <= 100:
                return amount * 5
            elif amount <= 300:
                return (100 * 5) + (amount - 100) * 7
            else:
                return (100 * 5) + (200 * 7) + (amount - 300) * 10

        case "Water":
            if amount <= 1000:
                return amount * 0.01
            elif amount <= 5000:
                return (1000 * 0.01) + (amount - 1000) * 0.015
            else:
                return (1000 * 0.01) + (4000 * 0.015) + (amount - 5000) * 0.02

        case "Gas":
            return 50 + amount * 8
        
        case _:
            return None

# ----- GUI Setup -----
def calculate():
    utility = utility_var.get()
    try:
        amount = float(amount_entry.get())
        if amount < 0:
            raise ValueError("Negative input")
        bill = estimate_bill(utility, amount)
        result_label.config(text=f"Estimated {utility} Bill: ₹{bill:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive number.")

# Main window
root = tk.Tk()
root.title("Utility Bill Estimator")
root.geometry("350x250")
root.resizable(False, False)

# Utility dropdown
utility_var = tk.StringVar(value="Electricity")
ttk.Label(root, text="Select Utility:", font=("Arial", 12)).pack(pady=5)
utility_menu = ttk.Combobox(root, textvariable=utility_var, values=["Electricity", "Water", "Gas"], state="readonly")
utility_menu.pack(pady=5)

# Amount entry
ttk.Label(root, text="Enter Usage:", font=("Arial", 12)).pack(pady=5)
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)

# Calculate button
ttk.Button(root, text="Estimate Bill", command=calculate).pack(pady=10)

# Result display
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
