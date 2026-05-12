print("💰 Expense Tracker (v5: dictionaries)")

expenses = [
    {"amount": 12.50, "category": "food",      "date": "2026-05-10"},
    {"amount": 45.00, "category": "transport", "date": "2026-05-11"},
    {"amount": 8.00,  "category": "food",      "date": "2026-05-12"},
]


menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Show total
  4) Summary by category
  5) Quit
"""

while True:
    print(menu)
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("  Amount: "))
        category = input("  Category: ")
        date = input("  Date (YYYY-MM-DD): ")
        expense = {
            "amount": amount,
            "category": category,
            "date": date,
        }
        expenses.append(expense)
        print(f"  ✅ Added.")

    elif choice == "2":
        print(f"  You have {len(expenses)} expenses:")
        for e in expenses:
            print(f"{e['date']:<12}{e['category']:<12}€{e['amount']:.2f}")
    
    elif choice == "3":
        total = 0
        for e in expenses:
            total = total + e["amount"]
        print(f"Total spent: €{total:.2f}")
        
    elif choice == "4":
        totals = {}
        for e in expenses:
            cat = e["category"]
            totals[cat] = totals.get(cat, 0) + e["amount"]

        for cat, amount in totals.items():
            print(f"  {cat:<12} €{amount:.2f}")


    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("  ⚠️  Invalid choice, try again.")
    

# Print every expense by its named fields
for e in expenses:
    print(f"  {e['date']:<12}{e['category']:<12}€{e['amount']:.2f}")
    
    
    print("💰 Expense Tracker")
        