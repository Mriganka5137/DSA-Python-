from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model, fuel, make):
        self.model = model
        self.fuel = fuel
        self.make = make
    
    @abstractmethod
    def get_fare(self):
        pass



class Car(Vehicle):
    def __init__(self, model, fuel, make, ac, sunroof):

        #Inherited attributes from parents
        Vehicle.model = model
        Vehicle.fuel = fuel
        Vehicle.make = make
        # Vehicle.__init__(self,model, fuel, make)


        #child attributes
        self.ac = ac
        self.sunroof = sunroof
    def get_fare(self):
        return self.fuel + " You are rich"

obj1 = Car('Tesla', 'Electric', 2019, True, True)
print(obj1.model)
print(obj1.get_fare())