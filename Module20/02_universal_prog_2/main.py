def is_prime(check_elem):
    count = 0

    if check_elem == 0 or check_elem == 1:
        return False
    elif check_elem == 2:
        return True

    for number in range(2, check_elem // 2 + 1):
        if check_elem % number == 0:
            count += 1
            break

    if count == 0:
        return True
    else:
        return False


def universal_prog_2(iter_object):
    return [elem for elem in iter_object if is_prime(iter_object.index(elem))]
