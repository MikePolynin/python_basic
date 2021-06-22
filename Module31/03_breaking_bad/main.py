import requests
import json


def breaking_bad() -> None:
    max_death = 0
    data_for_writing = {}

    my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
    data = json.loads(my_req.text)

    for record in data:
        if record['number_of_deaths'] > max_death:
            max_death = record['number_of_deaths']

    for record in data:
        if record['number_of_deaths'] == max_death:

            max_death_episode = requests.get('https://www.breakingbadapi.com/api/episodes')
            my_episode = json.loads(max_death_episode.text)

            season = record['season']
            episode_number = record['episode']
            number_of_deaths = record['number_of_deaths']
            names = record['death']

            for episode in my_episode:
                if int(episode['season']) == record['season'] and int(episode['episode']) == record['episode']:
                    print('Episode ID: {}'.format(episode['episode_id']))
                    data_for_writing['Episode ID'] = episode['episode_id']

            print('Season: {}'.format(season))
            data_for_writing['Season'] = season

            print('Episode: {}'.format(episode_number))
            data_for_writing['Episode'] = episode_number

            print('Death count: {}'.format(number_of_deaths))
            data_for_writing['Death count'] = number_of_deaths

            print('Names: {}'.format(names))
            data_for_writing['Names'] = names

    with open('BB_data.json', 'w') as file:
        json.dump(data_for_writing, file, indent=4)


breaking_bad()
