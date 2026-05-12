print("💰 Expense Tracker")

# Pre-fill some data so we have something to list
expenses = [
    [12.50, "food", "2026-05-10"],
    [45.00, "transport", "2026-05-11"],
    [8.00, "food", "2026-05-12"],
]

menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Quit
  4) Show total
"""

while True:
    print(menu)
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("  Amount: "))
        category = input("  Category: ")
        date = input("  Date (YYYY-MM-DD): ")
        expenses.append([amount, category, date])
        print(f"  ✅ Added.")

    elif choice == "2":
        print(f"  You have {len(expenses)} expenses:")
        for expense in expenses:
            print(f"{expenses[2]:<12}{expenses[1]:<12}€{expenses[3]:.2f}")

    elif choice == "3":
        print("👋 Goodbye!")
        break
    
    elif choice == "4":
        total = 0
        for expense in expenses:
            total = total + expense[0]      # amount is at index 0
        print(f"Total spent: €{total:.2f}")

    else:
        print("  ⚠️  Invalid choice, try again.")
    

    
        