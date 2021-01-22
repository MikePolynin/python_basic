quantity = int(input('Кол-во видеокарт: '))

old_list = []
new_list = []
max_num = 0

for i in range(quantity):
    v_card = int(input('%s Видеокарта: ' % (i + 1)))
    old_list.append(v_card)
    if v_card > max_num:
        max_num = v_card

for v_card in old_list:
    if v_card != max_num:
        new_list.append(v_card)

print('\nСтарый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)
