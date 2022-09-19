class Car():
    def __init__(self, model,fare):
        self.model = model
        self.fare = fare
    def __str__(self) -> str:
        return "This is a Uber fare class"
    def __add__(self,other):
        return self.fare + other.fare
    def __sub__(self,other):
        return self.fare - other.fare
car1 = Car("Tesla", 100)
car2 = Car("Mercedes", 500)
print(car1 - car2)