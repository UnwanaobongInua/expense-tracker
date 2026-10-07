import json
import os
from datetime import date

FILENAME = os.path.join(os.path.dirname(__file__), "expenses.json")


# Load saved expenses from the file (empty list if there is no file yet)
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


# Write the current list of expenses to the file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=2)


# Keep asking until the user enters a valid, positive number
def get_amount():
    while True:
        text = input("Amount: ")
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a valid number, like 12.5")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


# Ask for the details of a new expense and add it to the list
def add_expense(expenses):
    amount = get_amount()
    category = input("Category: ").lower()
    description = input("Description: ")

    new_expense = {
        "date": date.today().isoformat(),
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(new_expense)


# Print every expense, one per line
def list_expenses(expenses):
    print("All expenses:")
    for expense in expenses:
        print(
            expense.get("date", "no date"),
            "-",
            expense["amount"],
            "-",
            expense["category"],
            "-",
            expense["description"],
        )


# Add up the amount of every expense
def total_spent(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


# Build a dictionary of total spending per category
def category_summary(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals


# Print the spending totals for each category
def show_summary(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print("Spending by category:")
    totals = category_summary(expenses)
    for category, total in totals.items():
        print(category, "-", total)


expenses = load_expenses()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Category summary")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_expense(expenses)
        save_expenses(expenses)
    elif choice == "2":
        list_expenses(expenses)
    elif choice == "3":
        print("Total:", total_spent(expenses))
    elif choice == "4":
        show_summary(expenses)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 5.")