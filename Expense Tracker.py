import os
import datetime

EXPENSES_FILE = "expenses.txt"

expenses = []

# Function to display the list of expenses
def display_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        print("Expense List:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Date: {expense[0]}\n   Amount: {expense[1]}\n   Category: {expense[2]}\n   Description: {expense[3]}\n")

# Function to add an expense
def add_expense(amount, category, description):
    date = datetime.date.today()
    expenses.append((date, amount, category, description))
    print(f"Added expense: {amount} for {category} on {date}")

# Function to calculate total expenses for a specified time frame
def calculate_total_expenses(time_frame):
    today = datetime.date.today()
    total_expenses = 0
    for expense in expenses:
        if time_frame == 'daily' and expense[0] == today:
            total_expenses += expense[1]
        elif time_frame == 'weekly' and today - datetime.timedelta(days=7) <= expense[0] <= today:
            total_expenses += expense[1]
        elif time_frame == 'monthly' and today.month == expense[0].month:
            total_expenses += expense[1]
    return total_expenses

# Function to generate and display a monthly report
def generate_monthly_report():
    today = datetime.date.today()
    monthly_expenses = {}
    for expense in expenses:
        if today.month == expense[0].month:
            category = expense[2]
            amount = expense[1]
            if category not in monthly_expenses:
                monthly_expenses[category] = amount
            else:
                monthly_expenses[category] += amount
    if not monthly_expenses:
        print("No expenses for the current month.")
    else:
        print("Monthly Expense Report:")
        for category, amount in monthly_expenses.items():
            print(f"{category}: {amount:.2f}")

# Function to save expenses to a text file
def save_expenses():
    with open(EXPENSES_FILE, "w") as file:
        for expense in expenses:
            date_str = expense[0].strftime("%Y-%m-%d")
            file.write(f"{date_str},{expense[1]},{expense[2]},{expense[3]}\n")
    print("Expenses saved successfully.")

# Function to load expenses from a text file
def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                date_str, amount_str, category, description = line.strip().split(",")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                amount = float(amount_str)
                expenses.append((date, amount, category, description))
    except FileNotFoundError:
        print("No expense data found. Create a new expense to get started.")

# Main function
def main():
    load_expenses()
    while True:
        print("\nOptions:")
        print("1. Display expenses")
        print("2. Add expense")
        print("3. Calculate total expenses (daily, weekly, monthly)")
        print("4. Generate monthly report")
        print("5. Save expenses")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_expenses()
        elif choice == "2":
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            description = input("Enter a brief description: ")
            add_expense(amount, category, description)
        elif choice == "3":
            time_frame = input("Enter time frame (daily, weekly, monthly): ")
            total = calculate_total_expenses(time_frame)
            print(f"Total expenses for {time_frame} period: ${total:.2f}")
        elif choice == "4":
            generate_monthly_report()
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()