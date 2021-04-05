def registration():
    open('registrations_bad.log', 'w').close()
    open('registrations_good.log', 'w').close()
    data = list()
    try:
        with open('registrations.txt', 'r', encoding='utf-8') as file:
            with open('registrations_good.log', 'a', encoding='utf-8') as good_reg:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_reg:
                    for line in file:
                        try:
                            data = str(line).split(' ')
                            if len(data) != 3:
                                data.append('IndexError')
                                raise IndexError
                            for symbol in data[0]:
                                if not symbol.isalpha():
                                    data.append('NameError')
                                    raise NameError
                            if '@' not in data[1] or '.' not in data[1]:
                                data.append('SyntaxError')
                                raise SyntaxError
                            if int(data[2]) < 10 or int(data[2]) > 99:
                                data.append('ValueError')
                                raise ValueError
                            record = ' '.join(data)
                            good_reg.write(record)
                        except (IndexError, NameError, SyntaxError, ValueError):
                            record = ' '.join(data)
                            if '\n' in record:
                                record = record.replace('\n', '')
                            bad_reg.write(record + '\n')
    except FileNotFoundError:
        print('Файл с регистрационными данными не найден')


registration()
