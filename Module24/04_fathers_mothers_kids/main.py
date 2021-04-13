from kid import Kid
from parent import Parent


def father_mother_kid():
    kid_1 = Kid('Vasya', 5, True, False)
    kid_2 = Kid('Petya', 10, True, False)
    kid_3 = Kid('Ilya', 30, True, False)
    parent = Parent('Boris', 35, [kid_1, kid_2, kid_3])

    print(parent.kids[0].age)


father_mother_kid()
