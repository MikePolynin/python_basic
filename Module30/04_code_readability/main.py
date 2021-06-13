def code_readability():
    print('1 variant')
    for elem in (num for num in range(1, 100) if num == 1 or all(num % i != 0 for i in range(2, num))):
        print(elem)

    print('\n2 variant')
    for num in range(1, 100):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num)







if __name__ == '__main__':
    code_readability()
