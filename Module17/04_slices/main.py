def slices():
    alphabet = 'abcdefg'

    print('1:', alphabet[:])
    print('2:', alphabet[::-1])
    print('3:', alphabet[::2])
    print('4:', alphabet[1::2])
    print('5:', alphabet[:1])
    print('6:', alphabet[:len(alphabet) - 2:-1])
    print('7:', alphabet[3:4])
    print('8:', alphabet[len(alphabet) - 3:])
    print('9:', alphabet[len(alphabet) - 3:1:-1])
    print('10:', alphabet[2:len(alphabet) - 2])


slices()
