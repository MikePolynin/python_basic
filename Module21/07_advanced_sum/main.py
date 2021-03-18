def sum_count(numbers, result=0):
    for i, num in enumerate(numbers):
        if isinstance(num, int):
            result += num
        else:
            result += sum_count(num, 0)

    return result


def advanced_sum(numbers):
    if isinstance(numbers, int):
        print(numbers)
    else:
        print('Ответ:', sum_count(numbers))


advanced_sum([6, [3, 2], 2])
