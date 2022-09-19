from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def get_interest(self):
        pass
class SBI(Bank):
    def get_interest(self):
        return 3.5
obj1 = SBI()
print(obj1.get_interest())
    