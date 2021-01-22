user_word = input('Введите слово: ')

result = 0
symbols_count = []
checked_symbol = []

for i in range(len(user_word)):
    if user_word[i] not in checked_symbol:
        symbols_count.append(1)
        checked_symbol.append(user_word[i])
        for j in range(i + 1, len(user_word)):
            if user_word[i] == user_word[j]:
                symbols_count[i] += 1

for count in symbols_count:
    if count == 1:
        result += 1

print('Кол-во уникальных букв:', result)
