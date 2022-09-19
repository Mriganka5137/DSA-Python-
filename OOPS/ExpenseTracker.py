from datetime import date


class ExpenseTracker:
    """Class to Track Expense"""
    
    #Class Attribute
    expense_tracker_version = 1.0



    def __init__(self, date, description, amount, expense_type):
        self.date = date
        self.description = description
        self.amount = amount
        self.expense_type = expense_type

obj1 = ExpenseTracker("12 Aug", "Birthday Treat", 5000, "debit")
print(obj1.amount)

#Prints the object attributes in disctionary form
print(obj1.__dict__)

print(obj1.__getattribute__("date"))



#  getattr method takes in object and attribute name and returns value 
print(getattr(obj1,"description"))

# hasattr checks for the attribute ,if present return true else false
print(hasattr(obj1,"money"))  # False
print(hasattr(obj1,"amount")) # True


# delattr deletes the attribute given
#delattr(obj1,"expense_type")
print(obj1.__dict__)



print(getattr(obj1,"expense_type")) #AttributeError: 'ExpenseTracker' object has no attribute 'expense_type'


#calling the class attribute from the object
print(obj1.expense_tracker_version)