def files():
    filename = input('Название файла: ')

    spec_symbols = ('@', '№', '\u005C', '$', '%', '^', '&', '*', '(', ')')
    ends = ('.txt', '.docx')

    if filename.startswith(spec_symbols):
        print('\nОшибка: название начинается на один из специальных символов')
    elif not filename.endswith(ends):
        print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('\nФайл назван верно.')


files()
