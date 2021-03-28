def zen_of_python():
    zen = open('zen.txt', 'r')
    zen_reverse = []

    for line in zen:
        zen_reverse.append(line)

    zen.close()

    for i in range(len(zen_reverse) - 1, -1, -1):
        print(zen_reverse[i], end='')


zen_of_python()
