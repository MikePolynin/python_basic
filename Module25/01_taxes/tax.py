class Property:
    def __init__(self, worth):
        self.worth = worth
        self.tax = 0

    def count_tax(self):
        self.tax = self.worth
        return self.tax


class Apartment(Property):
    def __init__(self, worth, name):
        super().__init__(worth)
        self.name = name

    def count_tax(self):
        self.tax = self.worth / 1000
        return self.tax


class Car(Property):
    def __init__(self, worth, name):
        super().__init__(worth)
        self.name = name

    def count_tax(self):
        self.tax = self.worth / 200
        return self.tax


class CountryHouse(Property):
    def __init__(self, worth, name):
        super().__init__(worth)
        self.name = name

    def count_tax(self):
        self.tax = self.worth / 500
        return self.tax
