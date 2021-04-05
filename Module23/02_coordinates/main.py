import random


def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            with open('result.txt', 'w') as file_2:
                my_list = sorted([str(res1), str(res2), str(number)])
                file_2.write(' '.join(my_list))
except FileNotFoundError:
    print("Файла с координатами не найдено")
except ZeroDivisionError:
    print("На ноль делить нельзя")
