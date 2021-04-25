class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'
