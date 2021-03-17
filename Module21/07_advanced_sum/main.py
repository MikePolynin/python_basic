def sum_count(numbers, result=0):
    for i in range(len(numbers)):
        if isinstance(numbers[i], int):
            result += numbers[i]
        else:
            result += sum_count(numbers[i], 0)

    return result


def advanced_sum(numbers):
    if isinstance(numbers, int):
        print(numbers)
    else:
        print('Ответ:', sum_count(numbers))


advanced_sum([6, [3, 2], 2])
