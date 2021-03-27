def tournament():
    score = None
    output_data = dict()
    sorted_output_data = list()

    print('Содержимое файла {0}:'.format('first_tour.txt'))
    input_file = open('first_tour.txt', 'r')
    input_data = input_file.read().split('\n')
    input_file.close()

    for line in input_data:
        print(line)
        if score is None:
            score = int(line)
        else:
            result = line.split(' ')
            if int(result[2]) > score:
                new_name = result[1][0] + '. ' + result[0]
                output_data[new_name] = int(result[2])

    for index, user_score in enumerate(sorted(output_data.values(), reverse=True)):
        for key, value in output_data.items():
            if value == user_score:
                output_string = str(index + 1) + ') ' + key + ' ' + str(value) + '\n'
                sorted_output_data.append(output_string)

    print()
    print('Содержимое файла {0}:'.format('second_tour.txt'))
    output_file = open('second_tour.txt', 'w')

    output_file.write(str(len(sorted_output_data)) + '\n')
    for line in sorted_output_data:
        output_file.write(line)

    output_file.close()

    output_file = open('second_tour.txt', 'r')

    for line in output_file:
        print(line, end='')

    output_file.close()


tournament()
