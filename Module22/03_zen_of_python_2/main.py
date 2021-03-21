def zen_of_python_2():
    zen = open('zen.txt', 'r')
    symbol_count = 0
    word_count = 0
    line_count = 0
    letter_dict = dict()
    letters = []

    for line in zen:
        line_count += 1

        inp_str = line.split(' ')
        word_count += len(inp_str)

        for symbol in line:
            if symbol.isalpha():
                symbol_count += 1

                if symbol in letter_dict:
                    letter_dict[symbol] = letter_dict.pop(symbol) + 1
                else:
                    letter_dict[symbol] = 1

    zen.close()

    letter = max(letter_dict.values())

    for key, value in letter_dict.items():
        if value == letter:
            letters.append(key)

    print('В тексте {0} строк, {1} слов и {2} букв'.format(
        line_count,
        word_count,
        symbol_count))

    print('\nСамые частые буквы в тексте: ')
    for letter in letters:
        print(letter, end='\n')


zen_of_python_2()
