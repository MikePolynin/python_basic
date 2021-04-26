class Property:
    def __init__(self, worth, rate):
        self.worth = worth
        self.rate = rate
        self.tax = 0

    def count_tax(self):
        self.tax = self.worth / self.rate
        return self.tax


class Apartment(Property):
    def __init__(self, worth, name, rate=1000):
        super().__init__(worth, rate)
        self.name = name


class Car(Property):
    def __init__(self, worth, name, rate=200):
        super().__init__(worth, rate)
        self.name = name


class CountryHouse(Property):
    def __init__(self, worth, name, rate=500):
        super().__init__(worth, rate)
        self.name = name
