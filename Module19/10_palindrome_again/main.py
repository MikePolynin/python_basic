def palindrome_again():
    input_string = input('Введите строку: ')

    letters_dict = dict()
    palindrome = True

    for letter in input_string:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] = letters_dict.pop(letter) + 1

    if len(input_string) % 2 == 0:
        for letter in letters_dict:
            if letters_dict[letter] % 2 != 0:
                palindrome = False
                break

    else:
        count = 0
        for letter in letters_dict:
            if count > 1:
                palindrome = False
                break
            if letters_dict[letter] % 2 != 0:
                count += 1

        if count == 0:
            palindrome = False

    if palindrome:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


palindrome_again()
