def vowels():
    vowels_list = ['у', 'У', 'е', 'Е', 'ы', 'Ы', 'а', 'А', 'о', 'О', 'э', 'Э', 'я', 'Я', 'и', 'И', 'ю', 'Ю']

    user_str = list(input('Введите текст: '))

    result = [symbol for symbol in user_str if symbol in vowels_list]

    print('\nСписок гласных букв:', result)
    print('Длина списка:', len(result))


vowels()
