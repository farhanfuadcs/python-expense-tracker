# Python Expense Tracker

A simple command-line expense tracker built with Python. The program allows users to manage their expenses and calculate spending totals.

## Features

* Add expenses
* View all expenses
* Calculate total spending
* Find the highest expense
* Delete expenses
* Menu-driven command-line interface
* Input validation for menu choices and expense amounts

## Example

```text
1.Add Expenses
2.View Expenses
3.Total Spent
4.Highest Expense
5.Delete Expenses
6.Exit

Choose any option(1-6): 1

Enter the name of expense: food
Enter the amount: 500
Expense added!
```

Example of viewing expenses:

```text
food: 500, transport: 200, entertainment: 300
```

## Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Conditional statements
* Input validation
* List operations
* Built-in `sum()` function

## How to Run

Make sure Python is installed, then run:

```bash
python expense_tracker.py
```

## What I Practiced

This project helped me practice:

* Working with dictionaries
* Adding and removing dictionary items
* Creating functions
* Using `while` and `for` loops
* Validating user input
* Calculating totals
* Finding the highest value
* Using conditional statements
* Building a menu-driven CLI application

## Known Limitations

* Expense amounts currently accept only whole numbers.
* The program does not save expenses after the program is closed.
* Adding the same expense name again replaces its previous amount.
* There is no category or date tracking for expenses.

## Future Improvements

* Save expenses to a JSON or CSV file
* Support decimal amounts
* Add expense categories
* Add dates to expenses
* Add monthly spending summaries
* Add editing functionality
* Add a graphical or web interface
