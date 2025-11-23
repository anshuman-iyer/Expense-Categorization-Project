import json
import os

CATEGORIES = ["Food", "Travel", "Bills", "Other"]

KEYWORDS = {
    "Food": ["food", "restaurant", "lunch", "dinner", "breakfast", "snack", "groceries", "cafe", "pizza", "burger"],
    "Travel": ["bus", "train", "metro", "taxi", "uber", "ola", "flight", "fuel", "petrol", "diesel", "cab", "ticket"],
    "Bills": ["bill", "electricity", "water", "internet", "wifi", "phone", "mobile", "rent", "gas", "recharge"]
}

DATA_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def guess_category(description: str) -> str:
    desc = description.lower()
    for category, words in KEYWORDS.items():
        for w in words:
            if w in desc:
                return category
    return "Other"


def print_expenses_list(expenses):
    if not expenses:
        print("No expenses to show.\n")
        return
    print("\nIndex | Category |   Amount  | Description")
    print("-" * 50)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:5} | {e['category']:8} | {e['amount']:8.2f} | {e['description']}")
    print("")


def view_expenses(expenses):
    while True:
        print("\nView Expenses")
        print("1. View all")
        print("2. View by category")
        print("3. Search by text")
        print("4. Back to main menu")
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            print_expenses_list(expenses)
        elif choice == "2":
            print("Categories:", ", ".join(CATEGORIES))
            cat = input("Enter category name: ").strip().capitalize()
            if cat not in CATEGORIES:
                print("Unknown category.\n")
                continue
            filtered = [e for e in expenses if e["category"] == cat]
            print_expenses_list(filtered)
        elif choice == "3":
            q = input("Search text (in description): ").strip().lower()
            if not q:
                print("Empty search.\n")
                continue
            filtered = [e for e in expenses if q in e["description"].lower()]
            print_expenses_list(filtered)
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.\n")


def add_expense_flow(expenses):
    while True:
        amount_input = input("Amount (or 'b' to go back): ").strip()
        if amount_input.lower() == "b":
            return
        try:
            amount = float(amount_input)
        except ValueError:
            print("Invalid amount, try again.\n")
            continue

        description = input("Description: ").strip()
        category = guess_category(description)
        print(f"Suggested category: {category}")
        change = input("Press Enter to accept, or type a different category: ").strip()
        if change:
            change_cap = change.capitalize()
            if change_cap in CATEGORIES:
                category = change_cap
            else:
                print("Unknown category, using 'Other'.")
                category = "Other"

        expenses.append({
            "amount": amount,
            "description": description,
            "category": category
        })
        save_expenses(expenses)
        print("Saved.\n")


def print_summary(expenses):
    print("\n=== Expense Summary ===")
    totals = {c: 0.0 for c in CATEGORIES}
    for e in expenses:
        totals[e["category"]] += e["amount"]
    for c in CATEGORIES:
        print(f"{c}: {totals[c]:.2f}")
    print("")


def main():
    expenses = load_expenses()
    print("Expense Categorizer (with Save, Load & View)")
    print(f"Loaded {len(expenses)} existing expenses.\n")

    while True:
        print("Main Menu")
        print("1. Add expense")
        print("2. View older expenses")
        print("3. Summary")
        print("4. Quit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_expense_flow(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print_summary(expenses)
        elif choice == "4":
            print_summary(expenses)
            print("All data saved to 'expenses.json'.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

