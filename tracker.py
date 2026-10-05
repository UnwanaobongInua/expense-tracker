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
    {"amount": 5.25, "category": "food", "description": "breakfast"},
]

print("Add a new expense")
add_expense(expenses)
list_expenses(expenses)
print("Total:", total_spent(expenses))


