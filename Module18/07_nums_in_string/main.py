def nums_in_string():
    input_string = input('Введите строку: ')

    result = ''.join(input_string[i] for i in range(len(input_string)) if input_string[i].isdigit())

    print('Цифры:', result)


nums_in_string()
