expenses = [
    {"amount": 12.5, "category": "food", "description": "lunch"},
    {"amount": 40, "category": "transport", "description": "bus fare"},
    {"amount": 8.75, "category": "food", "description": "coffee"},
    {"amount": 5.25, "category": "food", "description": "breakfast"},
]

total = 0

print("All expenses:")
for expense in expenses:
    print(expense["amount"], "-", expense["category"], "-", expense["description"])
    total = total + expense["amount"]


print("Total:", total)

print(len(expenses))