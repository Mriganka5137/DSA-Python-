class Vehicle:
    def __init__(self, model, fuel, make):
        self.model = model
        self.fuel = fuel
        self.make = make
    
class Car(Vehicle):
    def __init__(self, model, fuel, make, ac, sunroof):
        super().__init__(model, fuel, make)
        self.ac = ac
        self.sunroof = sunroof

obj1 = Car("Tesla", "Electric", 2022, True, True)
print(obj1.__dict__)
        
