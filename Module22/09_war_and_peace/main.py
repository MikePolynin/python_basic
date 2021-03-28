import zipfile


def war_and_peace():
    alphabet = 'abcdefghijklmnopqrstuvwxyz' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    letter_dict = dict()
    letters_sum = 0
    uniq_freq = list()

    with zipfile.ZipFile('voyna-i-mir.zip') as text_file:
        text_file.extract('voyna-i-mir.txt')

    text_file.close()

    text = open('voyna-i-mir.txt', 'r', encoding='utf=8')
    for line in text:
        for symbol in line:
            if symbol in alphabet:
                if symbol in letter_dict:
                    letter_dict[symbol] = letter_dict[symbol] + 1
                else:
                    letter_dict[symbol] = 1

    text.close()

    for quantity in letter_dict.values():
        letters_sum += quantity

    for letter in letter_dict:
        letter_dict[letter] = round(letter_dict.get(letter) / letters_sum, 3)

    for freq in letter_dict.values():
        if freq in uniq_freq:
            continue
        else:
            uniq_freq.append(freq)

    output_file = open('analysis.txt', 'w')

    for freq in sorted(uniq_freq, reverse=True):
        for key, value in sorted(letter_dict.items()):
            if freq == value:
                output_file.write(key + ' ' + str(freq) + '\n')

    output_file.close()

    print()
    print('Содержимое файла {0}:'.format('analysis.txt'))
    output_file = open('analysis.txt', 'r')

    for line in output_file:
        print(line, end='')

    output_file.close()


war_and_peace()
