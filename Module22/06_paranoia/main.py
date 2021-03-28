def code(symbol, move):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

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


def paranoia():
    input_file = open('text.txt', 'r')
    output_file = open('cipher_text.txt', 'w')

    print('Содержимое файла text.txt:')
    for index, line in enumerate(input_file):
        print(line, end='')

        result = [code(line[i], index + 1) for i in range(len(line))]
        code_line = str.join('', result)

        output_file.write(code_line)

    input_file.close()
    output_file.close()

    output_file = open('cipher_text.txt', 'r')
    print()
    print('\nСодержимое файла cipher_text.txt:')

    for line in output_file:
        print(line, end='')

    output_file.close()


paranoia()
