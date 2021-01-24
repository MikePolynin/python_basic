def songs():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]

    selected_songs = []
    count = 0.00

    quantity = int(input('Сколько песен выбрать? '))
    for i in range(quantity):
        song = input('Название %d песни: ' % (i + 1))
        selected_songs.append(song)

    for selected_song in selected_songs:
        for violator_song in violator_songs:
            if selected_song == violator_song[0]:
                count += violator_song[1]

    print('\nОбщее время звучания песен:', round(count, 2), 'минут')


songs()
