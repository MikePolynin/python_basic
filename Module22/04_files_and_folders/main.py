import os

size = 0
dir_count = 0
file_count = 0


def files_and_folders(address):
    global size
    global dir_count
    global file_count

    for elem in os.listdir(address):
        if os.path.isdir(os.path.join(address, elem)):
            dir_count += 1
            files_and_folders(os.path.join(address, elem))
        else:
            file_count += 1
            size += os.path.getsize(os.path.join(address, elem))

    return size / 1024, dir_count, file_count


print('Размер каталога (в Кб): {0}\n'
      'Количество подкаталогов: {1}\n'
      'Количество файлов: {2}'.format(
    *files_and_folders(os.path.join('..', '..', '..', 'python_basic', 'Module14'))))
