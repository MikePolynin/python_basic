from kid import Kid


class Parent:
    def __init__(self, name='', age=0, children=list):
        self.name = name
        self.age = age
        self.kids = children

        for kid in self.kids:
            if self.age - kid.age <= 16:
                print('Некорректный возраст ребенка {}'.format(kid.name))

    def tell_name(self):
        return self.name

    def calm_kid(self, kid):
        if kid in self.kids and not kid.is_calm:
            kid.is_calm = True
            return True
        return False

    def feed_kid(self, kid):
        if kid in self.kids and kid.is_hungry:
            kid.is_hungry = False
            return True
        return False
