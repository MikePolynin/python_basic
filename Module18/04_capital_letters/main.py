def capital_letters():
    user_input = input('Введите строку: ')

    output_string = ' '.join(word[0].upper() + word[1:] for word in user_input.split())

    print('Результат: ' + output_string)


capital_letters()
