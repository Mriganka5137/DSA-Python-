class ExpenseTracker:
    """Class to Track Expense"""
    
    #Class Attribute
    expense_tracker_version = 1.0



    def __init__(self, date, description, amount, expense_type):
        self.date = date
        self.description = description
        
        # Private Attributes
        self.__amount = amount
        self.__expense_type = expense_type
    

    def get_description(self):
        return self.description

    def __get_date(self):
        return self.date

    @staticmethod
    def get_amount_format(amount):
        return float(amount)
    

    @classmethod
    def diary_input(cls,records:str):
        date, description, amount, expense_type = records.split(" ")
        return ExpenseTracker(date,description.capitalize(), cls.get_amount_format(amount), expense_type.capitalize())

day1 = ExpenseTracker("21 Aug", "Spent on Courses", 5000, "Credit")
# print(day1.amount) 
print(day1._ExpenseTracker__amount)  # This is how private values can be accessed in python

print(day1._ExpenseTracker__get_date()) # This is how to access the private methods of a class