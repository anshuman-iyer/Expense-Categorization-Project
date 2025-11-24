# Expense Categorizer – Personal Expense Tracker in Python

**🔹 Problem Statement**

People find it hard to track daily expenses and understand where most of their money is spent. Manual tracking is time-consuming and lacks insights. This project solves the problem by building a lightweight Python program that records expenses, categorizes them automatically, and summarizes spending.

**🔹 Functional Requirements**

The system has three major functional modules:

**1️⃣ Expense Input & Validation**

User enters amount + description

Amount is validated

q exits input mode and shows summary

**2️⃣ Automatic Category Detection**

Auto-suggests category (Food / Travel / Bills / Other) using keywords

User can accept suggestion or enter category manually

**3️⃣ Storage & Reporting**

Loads previous records from expenses.json

Saves all expenses on exit

Displays category-wise totals + full list

**🔹 Non-Functional Requirements (minimum 4)**

Usability – simple CLI, minimal input needed

Reliability – data saved persistently in JSON

Maintainability – modular code structure, editable keyword dictionary

Error Handling – invalid input handled gracefully

(Optional extras if needed: performance, resource efficiency)

**🔹 Architecture (short)**
main.py → handles user input
categorizer.py → category suggestion
storage.py → load/save JSON
report.py → summary printing
utils/validation.py → input checking

**🔹 Storage**

File: expenses.json
Sample data:

{"amount": 120.5, "description": "Pizza with friends", "category": "Food"}

**🔹 Features Summary (for README)
**
Add expense (amount + description)

Auto category detection via keywords

Manual override for category

Saves and loads data automatically

Shows category-wise spending summary

**🔹 statement.md (simple)**
The Expense Categorizer is a CLI tool that helps users record daily expenses and analyze spending pa
