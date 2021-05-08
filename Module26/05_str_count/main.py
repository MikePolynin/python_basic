import os


def file_line_count(address, count):
    with open(address, 'r') as file:
        for line in file:
            if line != len(line) * line[0]:
                if not line.startswith('#'):
                    count += 1
    return count


def str_count(address: str, count=0):
    norm_address = os.path.normpath(address)
    for elem in os.listdir(norm_address):
        if not os.path.isdir(os.path.join(norm_address, elem)) and elem.endswith('.py'):
            file_address = os.path.join(norm_address, elem)
            count = file_line_count(file_address, count)
        elif os.path.isdir(os.path.join(norm_address, elem)):
            directory = os.path.join(norm_address, elem)
            count = str_count(directory, count)
    return count


print(str_count('F:\\SkillBox\\python_basic\\Module26'))
