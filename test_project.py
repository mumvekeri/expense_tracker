# test_project.py

from project import add_expense, view_summary, filter_by_category, expenses

def test_add_expense():
    expenses.clear()
    add_expense()
    assert len(expenses) > 0
    assert "description" in expenses[0]
    assert "amount" in expenses[0]
    assert "category" in expenses[0]

def test_view_summary(capsys):
    expenses.clear()
    add_expense()
    view_summary()
    captured = capsys.readouterr()
    assert "Expense Summary" in captured.out

def test_filter_by_category(capsys):
    expenses.clear()
    expenses.append({"description": "Groceries", "amount": 50.0, "category": "Food"})
    filter_by_category()
    captured = capsys.readouterr()
    assert "Groceries" in captured.out
