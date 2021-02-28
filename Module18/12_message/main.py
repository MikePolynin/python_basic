def message():
    mes = input('Сообщение: ')

    words = mes.split(' ')
    new_message = []

    for i in range(len(words)):
        new_word = ''
        dif = 0
        for j in range(len(words[i])):

            if words[i][j].isalpha():

                while True:
                    if words[i][len(words[i]) - 1 - j - dif].isalpha():
                        break
                    else:
                        dif += 1

                new_letter = words[i][len(words[i]) - 1 - j - dif]

            else:
                new_letter = words[i][j]

            new_word += new_letter

        new_message.append(new_word)

    result = ' '.join(new_message)
    print('Новое сообщение:', result)


message()
