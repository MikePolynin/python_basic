import os

address_list = []
count = 0


def address_collector(address: str) -> None:
    global count
    norm_address = os.path.normpath(address)
    for elem in os.listdir(norm_address):
        if not os.path.isdir(os.path.join(norm_address, elem)) and elem.endswith('.py'):
            address_list.append(os.path.join(norm_address, elem))
        elif os.path.isdir(os.path.join(norm_address, elem)):
            directory = os.path.join(norm_address, elem)
            address_collector(directory)


def counter(addr_list: list) -> int:
    global count
    for addr in addr_list:
        with open(addr, 'r') as file:
            for line in file:
                if line != len(line) * line[0]:
                    if not line.startswith('#'):
                        count += 1

    return count


def str_count(address: str) -> int:
    address_collector(address)
    return counter(address_list)


print(str_count('F:\\SkillBox\\python_basic\\Module26'))
