def add_expense(expenses):
    """Prompt the user for one expense and append it to the list."""
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
    pass


def list_expenses(expenses):
    """Print all expenses in a formatted table."""
    print(f"  You have {len(expenses)} expenses:")
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<12}€{e['amount']:.2f}")
    pass


def show_summary(expenses):
    """Print total spent per category, plus an overall total."""
    totals = total_by_category(expenses)
    for cat, amount in totals.items():
        print(f"  {cat:<12} €{amount:.2f}")


def total_by_category(expenses) -> dict:
    """Compute and return a dictionary of total spending per category."""
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals 

def main():
    expenses = [
    {"amount": 12.50, "category": "food",      "date": "2026-05-10"},
    {"amount": 45.00, "category": "transport", "date": "2026-05-11"},
    {"amount": 8.00,  "category": "food",      "date": "2026-05-12"},
    ]
    
    menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Show summary by category
  4) Quit
"""
    while True:
        print(menu)
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        elif choice == "5":
            total_by_category(expenses)
        else:
            print("⚠️  Invalid choice, try again.")


if __name__ == "__main__":
    main()