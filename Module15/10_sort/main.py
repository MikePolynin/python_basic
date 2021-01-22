def find_min(some_list):
    min_val = some_list[0]

    for i in some_list:
        if i < min_val:
            min_val = i

    return min_val


start_list = [1, 4, -3, 0, 10]
result_list = []

print('Изначальный список:', start_list)

while len(start_list) > 0:
    number = find_min(start_list)
    result_list.append(number)
    start_list.remove(number)

print('Отсортированный список:', result_list)
