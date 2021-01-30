main_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

count_5 = 0
count_3 = 0

main_list.extend(side_list_1)

while True:
    if 5 in main_list:
        count_5 += 1
        main_list.remove(5)
    else:
        break

main_list.extend(side_list_2)

for digit in main_list:
    if digit == 3:
        count_3 += 1

print('Кол-во цифр 5 при первом объединении:', count_5)
print('Кол-во цифр 3 при втором объединении:', count_3)
print('Итоговый список:', main_list)
