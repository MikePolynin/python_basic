def check(ip):
    i = 0
    if len(ip) < 4:
        print('Адрес - это четыре числа, разделенные точками')
        return False
    else:
        while i < len(ip):
            if not ip[i].isdigit():
                print(ip[i], '- не целое число')
                return False
            elif int(ip[i]) > 255:
                print(ip[i], 'превышает 255')
                return False
            i += 1
        return True


def ip_address_2():
    input_ip = input('Введите IP: ')

    ip = input_ip.split('.')

    if check(ip):
        print('IP-адрес корректен')


ip_address_2()
