#Project: Expense Tracker - Installment 2
# Author: Fliance Eleu John M. Sadang
# Description: Accepts user input for expenses and displays a formatted summary.

#Banner
print("=" * 40)
print("     EXPENSE TRACKER")
print("  Know where your money goes.")
print("=" * 40)

#Main Menu
print("MAIN MENU")
print("   [1] View all expenses    (coming soon)")
print("   [2] Add an expense       (coming soon)")
print("   [3] Show total spent     (coming soon)")
print("   [4] Exit                 (coming soon)")

# Greeting & Yung Inputs
name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1= input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Calculations using required variable names
total = amount1 + amount2
average = total / 2

# Summary Output
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}: ${amount1}")
print(f"  - {item2}: ${amount2}")
print(f"Total spent: ${total}")
print(f"Average:     ${average}")
print("\n----------------------------------------")
print("Made by: Fliance Eleu John M. Sadang | Installment 2")

