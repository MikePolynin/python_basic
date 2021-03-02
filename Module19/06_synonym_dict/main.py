def synonym(syn_dict):
    user_word = input('Введите слово: ')

    for key in syn_dict:
        if key.lower() == user_word.lower():
            print('Синоним:', syn_dict[key])
        else:
            print('Такого слова в словаре нет.')
            synonym(syn_dict)
        break


def synonym_dict():
    syn_quantity = int(input('Введите количество пар слов: '))

    syn_dict = dict()

    for pair in range(syn_quantity):
        pair_str = input('{0} пара: '.format(pair + 1))
        word_list = pair_str.replace(' ', '').split('-')

        syn_dict[word_list[0]] = word_list[1]
        syn_dict[word_list[1]] = word_list[0]

        word_list.clear()

    print()
    synonym(syn_dict)


synonym_dict()
