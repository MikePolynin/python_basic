class Date:
    @classmethod
    def to_int_list(cls, input_date: str):
        numbers = None
        if '-' in input_date:
            try:
                numbers = [int(n) for n in input_date.split('-')]
            except ValueError:
                return None
        return numbers

    @classmethod
    def is_date_valid(cls, input_date: str) -> bool:
        if cls.to_int_list(input_date):
            numbers = cls.to_int_list(input_date)
            if len(numbers) != 3:
                return False
            elif numbers[1] == 1 or numbers[1] == 3 or numbers[1] == 5 or numbers[1] == 7 \
                    or numbers[1] == 8 or numbers[1] == 10 or numbers[1] == 12:
                if numbers[0] <= 0 or numbers[0] > 31:
                    return False
            elif numbers[1] == 4 or numbers[1] == 6 or numbers[1] == 9 or numbers[1] == 11:
                if numbers[0] <= 0 or numbers[0] > 30:
                    return False
            elif numbers[2] < 0:
                return False
            elif numbers[1] == 2:
                if numbers[2] % 4 == 0:
                    if 0 >= numbers[0] > 29:
                        return False
                    elif 0 >= numbers[0] > 28:
                        return False
            elif numbers[1] > 12:
                return False
        else:
            return False
        return True

    @classmethod
    def from_string(cls, input_date: str) -> str:
        if cls.is_date_valid(input_date):
            numbers = cls.to_int_list(input_date)
            return 'День: {day}     Месяц: {month}      Год: {year}' \
                .format(day=numbers[0],
                        month=numbers[1],
                        year=numbers[2])
        else:
            return 'False'
