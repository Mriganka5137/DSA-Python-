# Protected Attributes and methods are declared with one '_' underscore at the begining and can be accessed like 
# any regular attributes or methods


class Vehicle(object):
    def __init__(self, model, fuel, make):
        self.model = model
        self.fuel = fuel
        self.make = make
    
class Car(Vehicle):
    def __str__(self) -> str:
        return "This is class of CAR"
    def __init__(self, model, fuel, make, ac, sunroof):
        super().__init__(model, fuel, make)
        self._ac = ac               #protected
        self._sunroof = sunroof     # protected

obj1 = Car("Tesla", "Electric", 2022, True, True)
print(obj1.__dict__)
print(obj1._ac) # accessing protected variable
print(obj1)
