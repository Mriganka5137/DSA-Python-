class Student:
    """Class to learn various types of methods inside a class"""
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

    #attribute or object type method    
    def get_details(self):
        return self.name, self.roll_no, self.cgpa

    def check_grade(self,average=20):
        if self.cgpa > average:
            return self.cgpa
        else:
            return "You need to work hard"
    

    #This is how to define static method
    @staticmethod
    def check_value(amount):
        return float(amount)

s1 = Student("Mriganka", 5137, 10)
print(s1.get_details())
print(s1.check_value(5000))

print(s1.check_grade())

