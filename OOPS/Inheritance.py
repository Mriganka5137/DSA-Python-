class Vehicle():
    def __init__(self, model, fuel, make):
        self.model = model
        self.fuel = fuel
        self.make = make

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

obj1 = Car('Tesla', 'Electric', 2019, True, True)
print(obj1.model)
print(obj1.fuel)