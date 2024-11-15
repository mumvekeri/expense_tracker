# project.py

def main():
    """Main function to interact with the user."""
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter by Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

expenses = []

def add_expense():
    """Function to add an expense."""
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expenses.append({"description": description, "amount": amount, "category": category})
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_summary():
    """Function to view a summary of all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpense Summary:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']} ({expense['category']})")

def filter_by_category():
    """Function to filter expenses by category."""
    if not expenses:
        print("No expenses recorded.")
        return
    category = input("Enter category to filter by: ")
    filtered_expenses = [exp for exp in expenses if exp["category"].lower() == category.lower()]
    if not filtered_expenses:
        print("No expenses found for this category.")
    else:
        print("\nFiltered Expenses:")
        for expense in filtered_expenses:
            print(f"{expense['description']} - ${expense['amount']}")

if __name__ == "__main__":
    main()
