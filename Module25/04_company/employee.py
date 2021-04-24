from person import Person


class Employee(Person):
    def __init__(self, name, surname, age, rate):
        super().__init__(name, surname, age)
        self.rate = rate

    def get_salary(self):
        return self.rate


class Manager(Employee):
    def get_salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, rate, sales=0):
        super().__init__(name, surname, age, rate)
        self.sales = sales

    def get_salary(self):
        return 5000 + 0.05 * self.sales


class Worker(Employee):
    def __init__(self, name, surname, age, rate, hours=0):
        super().__init__(name, surname, age, rate)
        self.hours = hours

    def get_salary(self):
        return 100 * self.hours
