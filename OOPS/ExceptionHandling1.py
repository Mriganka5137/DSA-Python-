class Vehicle():
    def __init__(self, model, make, price):
        self.model = model
        self.make = make
        self.price = price

    def get_value(self):
        try:
            age = 2022 - self.make
            return 1000 * (1/age)
        except TypeError:
            try:
                age = 2022 - int(self.make)
                return 1000 * (1/age)
            except ZeroDivisionError:
                return 1000 * 1
            except:
                return "You have entered wrong format"
        except ZeroDivisionError:
            age = 2022 - self.make
            return 1000 * 1

obj1 = Vehicle("Tesla", 2022, 600000)
print(obj1.get_value())
