films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
user_list = []

while True:
    film = input('Введите название фильма: ')
    if film == 'exit' or film == 'Exit':
        break
    elif film in films:
        user_list.append(film)
    else:
        print('Такого фильма нет')

print('\nВаши любимые фильмы:')
for _ in user_list:
    print(_)
