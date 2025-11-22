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


def main():
    expenses = load_expenses()

    print("Expense Categorizer (with Save & Load)")
    print(f"Loaded {len(expenses)} existing expenses.\n")
    print("Enter expenses (type 'q' for amount to quit)\n")

    while True:
        amount_input = input("Amount (or 'q' to finish): ").strip()
        if amount_input.lower() == "q":
            break

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

        save_expenses(expenses)  # save immediately
        print("Saved.\n")

    # Summary
    print("\n=== Expense Summary ===")
    totals = {c: 0.0 for c in CATEGORIES}

    for e in expenses:
        totals[e["category"]] += e["amount"]

    for c in CATEGORIES:
        print(f"{c}: {totals[c]:.2f}")

    print("\nDetailed list:")
    for e in expenses:
        print(f"{e['category']:6} | {e['amount']:8.2f} | {e['description']}")

    print("\nAll data saved to 'expenses.json'.")


if __name__ == "__main__":
    main()
