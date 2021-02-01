def reversal():
    input_str = input('Введите строку: ')

    h_i = [i for i in range(len(input_str)) if input_str[i] == 'h']
    result = [input_str[h_i[i + 1]:h_i[i]:-1] for i in range(len(h_i) - 1)]
    result_str = input_str[:h_i[0]] + str.join('', result) + input_str[h_i[len(h_i) - 1]:]

    print('Измененная строка: ' + result_str)


reversal()
