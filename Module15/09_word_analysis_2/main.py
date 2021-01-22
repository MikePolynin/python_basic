word = input('Введите слово: ')

if len(word) % 2 == 0:
    middle = len(word) // 2
else:
    middle = len(word) // 2

first_part = word[:middle]
second_part = word[-1:-middle - 1:-1]

if first_part == second_part:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')