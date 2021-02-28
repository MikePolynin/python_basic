def compression():
    input_string = input('Введите строку: ')
    result = []

    i = 0
    letter_count = 1

    while i < len(input_string) - 2:
        result.append(input_string[i])
        j = i + 1
        while input_string[i] == input_string[j] and j < len(input_string) - 1:
            letter_count += 1
            j += 1
        result.append(str(letter_count))
        i += letter_count
        letter_count = 1
    if input_string[-1] != result[-2]:
        result.append(input_string[-1])
        result.append('1')
    else:
        result[-1] = str(int(result[-1]) + 1)

    result_string = ''.join(result)

    print(result_string)


compression()
