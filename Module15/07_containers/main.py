def check_weight(new_weight):
    while True:
        if isinstance(new_weight, int) and 0 < new_weight <= 200:
            break
        else:
            print('Некорректный ввод')
            check_weight(int(input('Введите корректный вес контейнера: ')))
        break


container_list = []
result = 0

quantity = int(input('Кол-во контейнеров: '))

for container in range(quantity):
    weight = int(input('Введите вес контейнера: '))
    check_weight(weight)
    container_list.append(weight)

new_container_weight = int(input('\nВведите вес нового контейнера: '))
check_weight(new_container_weight)

if new_container_weight > container_list[0]:
    result = 1
elif new_container_weight <= container_list[-1]:
    result = len(container_list) + 1
elif len(container_list) >= 3:
    for i in range(1, len(container_list) - 1):
        if container_list[i - 1] >= new_container_weight > container_list[i]:
            result = i + 1
else:
    result = 2

print('\nНомер, куда встанет новый контейнер:', result)
