def code(symbol, move):
    lowercase = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    capital = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
               'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    if symbol in lowercase:
        index = lowercase.index(symbol) + move
        if index >= 33:
            index -= 33
        return lowercase[index]
    elif symbol in capital:
        index = capital.index(symbol) + move
        if index >= 33:
            index -= 33
        return capital[index]
    else:
        return symbol


def caesar_cipher():
    user_str = input('Введите сообщение: ')
    move = int(input('Введите сдвиг: '))

    result = [code(user_str[i], move) for i in range(len(user_str))]

    print('Зашифрованное сообщение: ' + str.join('', result))


caesar_cipher()
