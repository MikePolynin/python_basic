def longest_word():
    input_string = input('Введите строку: ')

    words = input_string.split()

    words_length = [len(words[i]) for i in range(len(words))]
    words_length.sort()

    max_length = words_length[len(words_length) - 1]

    longest_words = [words[word_i] for word_i in range(len(words)) if len(words[word_i]) == max_length]

    result = 'Самые длинные слова в строке: {0}, максимальная длина {1}'.format(
        longest_words,
        max_length
    )

    print(result)


longest_word()
