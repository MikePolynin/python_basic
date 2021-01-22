quantity = int(input('Кол-во клеток: '))

efficiency = []
wrong_efficiency = []

for i in range(quantity):
    efficiency_i = int(input('Эффективность %s клетки: ' % (i + 1)))
    efficiency.append(efficiency_i)

for i in range(len(efficiency)):
    if efficiency[i] < i:
        wrong_efficiency.append(efficiency[i])

print('\nНеподходящие значения:', wrong_efficiency)
