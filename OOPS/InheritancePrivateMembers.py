class Vehicle():
    def __init__(self, model, fuel, make):
        self.__model = model
        self.fuel = fuel
        self.make = make
    def __private_method_parent(self):
        print("Inside Private part of Parent")

class Car(Vehicle):
    def __init__(self, model, fuel, make, ac, sunroof):

        #Inherited attributes from parents
        Vehicle.__model = model
        Vehicle.fuel = fuel
        Vehicle.make = make
        # Vehicle.__init__(self,model, fuel, make)


        #child attributes
        self.__ac = ac
        self.sunroof = sunroof

    def showParent_attribute(self):
        print(Vehicle.__model)
    def showPrivateMethodOfParent(self):
        self._Vehicle__private_method_parent()


obj1 = Car('Tesla', 'Electric', 2019, True, True)

#This is how we access the private attribute of any class
print(obj1._Car__ac) 


obj1.showParent_attribute()

obj1.showPrivateMethodOfParent()
