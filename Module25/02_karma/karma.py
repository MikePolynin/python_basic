import random

from karma_except import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError


def one_day():
    karma_level = random.randint(1, 7)
    exception = random.randint(1, 10)
    if exception == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    else:
        return karma_level


class Karma:
    karma_level = 0
    day = 1
    log = []

    while karma_level < 500:
        try:
            karma_day_level = one_day()
            karma_level += karma_day_level
            print('Day {}, karma_level {}'.format(day, karma_level))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as day_except:
            log_line = 'Day {}, mistake: {}'.format(day, day_except)
            log.append(log_line)
            print(log_line)
        day += 1

    with open('karma.log', 'w') as karma_log:
        for line in log:
            karma_log.write(line + '\n')
