class NegativeCarValue(Exception):
    def __init__(self, value, message ="Car value cannot be negative"):
        self.value = value
        self.message = message 
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} --> {self.value}'


class Car:
    def __init__(self, model, make, fuel) -> None:
        self.model = model
        self.make = make
        self.fuel = fuel
        self.current_year = 2021

    def get_value(self):
        age = self.current_year - self.make

        if age < 0 :
            raise NegativeCarValue(age)
        else:
            return 1000 * (1/age)

obj1 = Car("Tesla", 2022, "Electric")
print(obj1.get_value())
