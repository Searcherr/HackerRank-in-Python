from abc import ABCMeta, abstractmethod
import copy


class StudentPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone(self):
        #deepcopy from copy
        pass
class Address:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}"


class Student(StudentPrototype):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name} lives at {self.address}"

    def clone(self):
        return copy.deepcopy(self)


maria = Student('Maria', 'Teresa', Address('Poland', 'Warsaw', 'Jana Pawla II'))
print(maria)
print('---------------')
franz = maria.clone()
franz.first_name = 'Franz'
franz.last_name = 'Stephan'
print(franz, '\n', maria)

print(maria.__dict__)
print(franz.__dict__)

print(hash(maria))
print(hash(franz))