def frequency_analysis():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = dict()
    letters_sum = 0
    uniq_freq = list()

    print('Содержимое файла {0}:'.format('text.txt'))
    input_file = open('text.txt', 'r')
    for line in input_file:
        print(line, end='')
        for symbol in line:
            if symbol.lower() in alphabet:
                if symbol.lower() in letter_dict:
                    letter_dict[symbol.lower()] = letter_dict.pop(symbol) + 1
                else:
                    letter_dict[symbol.lower()] = 1
    print()
    input_file.close()

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


frequency_analysis()
