class Vehicle:
    current_year = 2022
    base_price_factor = 2 
    def __init__(self, model, fuel, make):
        self.model = model
        self.fuel = fuel
        self.make = make
    def get_value(self):
        age = Vehicle.current_year - self.make
        return ((1/Vehicle.base_price_factor)*5000000)//age

class Car(Vehicle):
    base_price_factor = 5
    def __init__(self, model, fuel, make, ac, sunroof):
        super().__init__(model, fuel, make)
        self.ac = ac
        self.sunroof = sunroof

    def get_value(self):
        age = Vehicle.current_year - self.make
        print("This is child here yo")
        return ((1/self.base_price_factor)*5000000)//age

obj1 = Car("Tesla", "Electric", 2021, True, True)
print(obj1.__dict__)
print(obj1.get_value())

# obj2 = Vehicle("Ford", "Petrol", 2021)
# print(obj2.get_value())
        
