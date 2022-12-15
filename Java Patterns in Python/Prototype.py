class StateAndCity:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}"
class Student:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.state_and_city = address

    def __str__(self):
        return f"{self.first_name}, {self.last_name} is in the {self.address}'s group"


