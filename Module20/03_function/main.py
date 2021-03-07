def function(user_tuple, user_symbol):
    result_tuple = tuple()

    if user_symbol in user_tuple:
        first_index = user_tuple.index(user_symbol)
        last_index = first_index

        if user_symbol in user_tuple[first_index + 1:]:
            last_index = user_tuple.index(user_symbol, first_index + 1)

        result_tuple = user_tuple[first_index: last_index + 1]

    return result_tuple


function((2, 3, 4, 2, 5, 6), 2)
