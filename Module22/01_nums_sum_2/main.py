def nums_sum_2():
    total_sum = 0

    input_file = open('numbers.txt', 'r')
    print('Содержимое файла numbers.txt')
    for line in input_file:
        print(line, end='')
        for symbol in line:
            if symbol.isdigit():
                total_sum += int(symbol)
    input_file.close()

    answer_file = open('answer.txt', 'w')
    answer_file.write(str(total_sum))
    answer_file.close()

    print()
    answer_file = open('answer.txt', 'r')
    print('\nСодержимое файла answer.txt')
    for line in answer_file:
        print(line, end='')
    answer_file.close()


nums_sum_2()

