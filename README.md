# 🧾 Expense Categorizer (with Save & Load)

A simple Python program that helps you record your daily expenses and automatically categorizes them into Food, Travel, Bills, or Other using smart keyword detection. Your data is saved to a file and loaded back every time you run the program.

# 🚀 Features

✔ Add expenses with amount and description
✔ Automatic category detection from keywords
✔ Option to manually change category
✔ Saves all expenses to expenses.json
✔ Automatically loads past expenses on startup
✔ Displays category-wise total and full expense list

# 📂 File Storage

All expense records are stored in a local JSON file:

expenses.json


Each expense entry looks like:
```
{
  "amount": 120.5,
  "description": "Pizza with friends",
  "category": "Food"
}
```
# ▶ How to Run

Install Python 3

Download the project files

Run the program:
```
python main.py
```

(replace main.py with the actual filename if different)

# 🧠 Usage

Enter amount

Enter description

The program will suggest a category automatically

Press Enter to accept or type another category:

>  Food
>  Travel
>  Bills
>  Other

Type q instead of amount to quit and view summary

# 📊 Output Summary

At the end of a session, you'll see:
```
=== Expense Summary ===
Food: 450.00
Travel: 200.00
Bills: 1200.00
Other: 150.00

Detailed list:
Food   |  150.00 | Pizza with friends
Travel |  200.00 | Bus ticket
Bills  | 1200.00 | Electricity bill
...
```
# 🔧 Customization

You can change keyword detection inside the dictionary:
```
KEYWORDS = {
    "Food": ["pizza", "burger", "cafe", ...],
    "Travel": ["bus", "metro", "flight", ...],
    "Bills": ["electricity", "rent", ...]
}
