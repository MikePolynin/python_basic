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

    open('karma.log', 'w').close()

    while karma_level < 500:
        try:
            karma_day_level = one_day()
            karma_level += karma_day_level
            print('Day {}, karma_level {}'.format(day, karma_level))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as day_except:
            log_line = 'Day {}, mistake: {}'.format(day, day_except)
            print(log_line)
            with open('karma.log', 'a') as karma_log:
                karma_log.write(log_line + '\n')
        day += 1
