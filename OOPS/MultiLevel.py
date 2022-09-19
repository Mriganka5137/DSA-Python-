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


class ElectricCar(Car):
    def __init__(self, model, fuel, make, ac, sunroof, distance):
        super().__init__(model, fuel, make, ac, sunroof)
        self.distance = distance
Tesla = ElectricCar("X", "Electric", 2022, True, True, 500)
print(Tesla.__dict__)