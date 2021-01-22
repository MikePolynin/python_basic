move = int(input('Сдвиг: '))

start_list = [1, 2, 3, 4, 5]
result_list = []

if move >= len(start_list):
    move -= len(start_list)

for i in range(-move, 0):
    result_list.append(start_list[i])
for i in range(-len(start_list), -move):
    result_list.append(start_list[i])

print('Изначальный список:', start_list)
print('Сдвинутый список:', result_list)
