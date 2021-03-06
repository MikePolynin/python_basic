def players_func():
    players = {
        ("Ivan", "Volkin"): (10, 5, 13),
        ("Bob", "Robbin"): (7, 5, 14),
        ("Rob", "Bobbin"): (12, 8, 2)
    }

    new_players = [(player_name + player_score) for player_name, player_score in players.items()]

    print(new_players)


players_func()
