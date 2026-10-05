def add_expense(expense):
    amount = float(input("Amount: "))
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
    
def total_spent(expense):
    total = 0
    for expense in expenses:    
        total = total + expense["amount"]
    return total


expenses = [
    {"amount": 12.5, "category": "food", "description": "lunch"},
    {"amount": 40, "category": "transport", "description": "bus fare"},
    {"amount": 8.75, "category": "food", "description": "coffee"},
]

while True:
    print("\n--- Expense Tacker ---")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Quit")

    choice = input("Choice an option (1-4): ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        list_expenses(expenses)
    elif choice == "3":
        print("Total:", total_spent(expenses))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.")

    




