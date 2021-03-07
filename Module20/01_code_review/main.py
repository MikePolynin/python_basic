def students_func(students_dict):
    lst = set()
    cnt = 0

    for i in students_dict.values():
        for interest in i['interests']:
            lst.add(interest)

        for surname in i['surname']:
            cnt += len(surname)

    interests_str = ', '.join(lst)

    return interests_str, cnt


def code_review():
    students = {
        1: {
            'name': 'Bob',
            'surname': 'Vazovski',
            'age': 23,
            'interests': ['biology, swimming']
        },
        2: {
            'name': 'Rob',
            'surname': 'Stepanov',
            'age': 24,
            'interests': ['math', 'computer games', 'running']
        },
        3: {
            'name': 'Alexander',
            'surname': 'Krug',
            'age': 22,
            'interests': ['languages', 'health food']
        }
    }

    for student_id, student_age in students.items():
        print('Student`s id: {0}, student`s age: {1}'.format(student_id, student_age['age']))

    result = students_func(students)

    print('\nStudents interests are: {0}'.format(result[0]))
    print('\nTotal student`s surnames length: {0}'.format(result[1]))


code_review()
