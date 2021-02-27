def counting(expression):
    numbers = []
    action = []
    number = ''

    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '*' or expression[i] == '/':
            action.append(expression[i])
            numbers.append(int(number))
            number = ''
        elif expression[i] == '-' and not expression[i - 1].isdigit():
            number += expression[i]
        elif expression[i] == '-' and expression[i - 1].isdigit():
            action.append(expression[i])
            numbers.append(int(number))
            number = ''
        else:
            number += expression[i]

    numbers.append(int(number))

    i = 0
    while True:

        if len(action) == 0 or ('*' not in action and '/' not in action):
            break

        if action[i] == '*':
            numbers[i] = numbers[i] * numbers[i + 1]
            numbers = numbers[:i + 1] + numbers[i + 2:]
            action = action[:i] + action[i + 1:]
            i = 0
            continue

        elif action[i] == '/':
            numbers[i] = numbers[i] / numbers[i + 1]
            numbers = numbers[:i + 1] + numbers[i + 2:]
            action = action[:i] + action[i + 1:]
            i = 0
            continue

        elif action[i] == '+' or action[i] == '-':
            i += 1
            continue

        i += 1

    while True:
        i = 0

        if len(action) == 0:
            break

        if action[i] == '+':
            numbers[i] = numbers[i] + numbers[i + 1]
            numbers = numbers[:i + 1] + numbers[i + 2:]
            action = action[:i] + action[i + 1:]
            continue

        elif action[i] == '-':
            numbers[i] = numbers[i] - numbers[i + 1]
            numbers = numbers[:i + 1] + numbers[i + 2:]
            action = action[:i] + action[i + 1:]
            continue

        i += 1

    if numbers[0] < 0:
        return str(numbers[0])
    else:
        return str(numbers[0])


def parentheses(expression):
    first = expression.index('(')
    start_index = first
    finish_index = 0

    for i in range(first, len(expression)):
        if expression[i] == ')':
            finish_index = i
            break
        elif expression[i] == '(':
            start_index = i

    new_expression = expression[start_index + 1: finish_index]

    counted_expression = counting(new_expression)

    result = expression[:start_index] + counted_expression + expression[finish_index + 1:]

    return result


def math():
    expression = input('Выражение: ')

    while '(' in expression:
        expression = parentheses(expression)

    answer = counting(expression)

    print('\nОтвет:', answer)


math()
