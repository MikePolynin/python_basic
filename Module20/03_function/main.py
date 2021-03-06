def function(user_tuple, user_symbol):
    result_tuple = tuple()

    if user_symbol in user_tuple:
        count = 0

        for symbol in user_tuple:
            if symbol == user_symbol:
                count += 1
            if count == 2:
                break

        first_index = user_tuple.index(user_symbol)

        if count == 1:
            last_index = len(user_tuple) - 1
        else:
            last_index = user_tuple.index(user_symbol, first_index + 1, len(user_tuple))

        result_tuple = user_tuple[first_index: last_index + 1]

    return result_tuple
