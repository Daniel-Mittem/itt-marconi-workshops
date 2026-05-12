print("💰 Expense Tracker — add an expense")

amount_str = input("Amount: ")
amount = float(amount_str)
date = input("Date (DD-MM-YYYY):")
category = input("Category: ").strip()

print(f"Recorded: €{amount:.2f} - {category} - {date}.")