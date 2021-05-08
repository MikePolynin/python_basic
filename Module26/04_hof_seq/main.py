def hof_seq() -> None:
    from QHofstadter import QHofstadter

    my_hofstadter = QHofstadter([1, 1])

    [next(my_hofstadter) for _ in range(10)]

    print(my_hofstadter.numbers_list)


hof_seq()
