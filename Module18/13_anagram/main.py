def anagram():
    word_1 = input('Введите 1 слово: ')
    word_2 = input('Введите 2 слово: ')

    checked_symbol = []
    symbols_count = []

    if len(word_1) != len(word_2):
        print('\nСлова не являются анаграммами друг друга')
    else:
        for i in range(len(word_1)):
            if word_1[i] not in checked_symbol:
                checked_symbol.append(word_1[i])
                symbols_count.append(1)
            else:
                symbols_count[checked_symbol.index(word_1[i])] += 1

        for i in range(len(checked_symbol)):
            count = 0
            for j in range(len(word_2)):
                if word_2[j] == checked_symbol[i]:
                    count += 1

            if count != symbols_count[i]:
                print('\nСлова не являются анаграммами друг друга')
                break

        print('\nСлова являются анаграммами друг друга')


anagram()
