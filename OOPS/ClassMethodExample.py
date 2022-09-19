class ExpenseTracker:
    """Class to Track Expense"""
    
    #Class Attribute
    expense_tracker_version = 1.0



    def __init__(self, date, description, amount, expense_type):
        self.date = date
        self.description = description
        self.amount = amount
        self.expense_type = expense_type
    
    @staticmethod
    def get_amount_format(amount):
        return float(amount)
    

    @classmethod
    def diary_input(cls,records:str):
        date, description, amount, expense_type = records.split(" ")
        return ExpenseTracker(date,description.capitalize(), cls.get_amount_format(amount), expense_type.capitalize())

day1 = ExpenseTracker("21 Aug", "Spent on Courses", 5000, "Credit")
print(day1.amount)
day2 = ExpenseTracker.diary_input("22-Aug spent_on_shoes 50000 credit")
print(day2.description)
print(day2.amount)