nums = dict()


def calculating_math_func(data):
    global nums

    if data in nums:
        result = nums[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        nums[data] = result

    result /= data ** 3
    result = result ** 10
    return result


def make_function_faster():
    while True:
        number = int(input('Введите число: '))

        print(calculating_math_func(number))


make_function_faster()
