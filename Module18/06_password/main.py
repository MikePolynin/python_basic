def upper_check(user_password):
    for i in range(len(user_password)):
        if user_password[i].isupper():
            return True


def digit_check(user_password):
    count = 0
    for i in range(len(user_password)):
        if user_password[i].isdigit():
            count += 1
    if count >= 3:
        return True


def password():
    while True:
        user_password = input('Придумайте пароль: ')
        if len(user_password) < 8:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
        elif not upper_check(user_password):
            print('Пароль ненадёжный. Попробуйте ещё раз.')
        elif not digit_check(user_password):
            print('Пароль ненадёжный. Попробуйте ещё раз.')
        else:
            print('Это надёжный пароль!')
            break


password()
