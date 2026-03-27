# 💰 Expense Tracker (Python CLI App)

##  Overview

**Expense Tracker** is a simple command-line application built in Python that helps users manage their daily expenses efficiently. It allows users to add, view, filter, and analyze their expenses in an organized way.

---

## 🚀 Features

```
===== Expense Tracker =====

1. Add Expense
2. View Expenses
3. Filter Expenses
4. Total Expense (Category-Wise)
5. Total Expense (All)
6. Exit
```

### 🔹 1. Add Expense

* Add a new expense with details such as:

  * Amount
  * Category

### 🔹 2. View Expenses

* Displays all recorded expenses in a structured format.

### 🔹 3. Filter Expenses

* Filter expenses based on:

  * Category

### 🔹 4. Total Expense (Category-Wise)

* Shows total spending grouped by categories.

### 🔹 5. Total Expense (All)

* Displays the total of all recorded expenses.

### 🔹 6. Exit

* Safely exits the application.

---

## 🛠️ Project Structure

```
Expense_Tracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # Entry point of the application
│   ├── expense.py     # Core logic (add, view, filter, etc.)
│   └── storage.py       # Helper functions (if any)
│
├── data/
│   └── expenses.json  # Stores expense data
│
└── README.md
```

---

## ▶️ How to Run

Make sure you are in the root folder of the project, then run:

```bash
python -m app.main
```

---

## 📦 Requirements

* Python 3.x

(No external libraries required if using standard library)

---
