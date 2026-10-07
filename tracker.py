import json
import os

FILENAME = os.path.join(os.path.dirname(__file__), "expenses.json")


def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=2)

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

def add_expense(expenses):
    amount = get_amount()
    category = input("Category: ")
    description = input("Description: ")

    new_expense = {
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(new_expense)


def list_expenses(expenses):
    print("All expenses:")
    for expense in expenses:
        print(expense["amount"], "-", expense["category"], "-", expense["description"])


def total_spent(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total

expenses = load_expenses()


def category_summary(expense):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals

def show_summary(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print("spending by category:")
    totals = category_summary(expenses)
    for category, total in totals.items():
        print(category, "-", total)

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
    




