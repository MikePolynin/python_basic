import itertools


def pin_code() -> None:
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for pin_code_variant in itertools.combinations_with_replacement(digits, 4):
        print(pin_code_variant)


pin_code()
