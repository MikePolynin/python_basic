import re


def check(number) -> str:
    phone_number_pattern = r'\b[8.9]\d{9}\b'
    result = re.match(phone_number_pattern, number)

    if result:
        return 'всё в порядке'
    else:
        return 'не подходит'


def phone_numbers() -> None:
    numbers = ['9999999999', '999999-999', '99999x9999']

    for i in range(len(numbers)):
        print('{0} номер: {1}'.format(i, check(numbers[i])))


phone_numbers()
