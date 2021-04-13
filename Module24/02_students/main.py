from student import Student
import random


def students():
    names = ['Ivan', 'Petr', 'Andrey', 'Vasiliy', 'Pavel', 'Oleg', 'Ilya', 'Kirill', 'Dmitriy', 'Aleksey']
    ave_score_dict = dict()

    students_list = [Student(names[i], random.randint(1, 10), [random.randint(1, 5) for _ in range(5)])
                     for i in range(10)]

    for student in students_list:
        ave_score = 0
        for score in student.progress:
            ave_score += score
        ave_score_dict[student] = round(ave_score / 5, 2)

    for ave_score in sorted(set(ave_score_dict.values())):
        for student, score in ave_score_dict.items():
            if ave_score == score:
                print('Средний балл: {}, ФИ студента: {}'.format(score, student.name))


students()
