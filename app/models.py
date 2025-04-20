import csv
import os

class User:
    def __init__(self, form_data):
        self.age = int(form_data['age'][0])
        self.gender = form_data['gender'][0]
        self.income = float(form_data['income'][0])

        # Define expected categories
        self.expense_categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        self.expenses = {
            cat: float(form_data.get(cat, [0.0])[0]) for cat in self.expense_categories
        }

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            **self.expenses
        }

    def save_to_csv(self):
        # Absolute file path
        filepath = os.path.join(os.path.dirname(__file__), 'data', 'users.csv')
        headers = ["age", "gender", "income"] + self.expense_categories

        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        file_exists = os.path.isfile(filepath)
        with open(filepath, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow(self.to_dict())
