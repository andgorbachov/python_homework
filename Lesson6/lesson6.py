
def all_sizes_from_international(sizes_dict, inter_size):
    size_table = {}
    index = 0
    for i, size in enumerate(sizes_dict['International']):
        if size == inter_size:
            index = i
            break
    for key, value in sizes_dict.items():
        for i, s in enumerate(value):
            if i == index:
                size_table.update({key: s})
    return size_table

# ----------------------------------
# """Задание 3"""


# def get_students_with(students_courses, attend_courses):
#     student_list = []
#     for st, cs, in students_courses.items():
#         [student_list.append(st) for c in attend_courses if cs.__contains__(c)]
#     return list(set(student_list))


def get_students_with(students_courses, attend_courses):
    student_list = []
    for st, cs, in students_courses.items():
        for c in attend_courses:
            if cs.__contains__(c):
                student_list.append(st)
                break
    return student_list


def get_students_without(students_courses, unattended_courses):
    student_list = []
    for st, cs in students_courses.items():
        no_course = True
        for c in unattended_courses:
            if cs.__contains__(c):
                no_course = False
                break
            else:
                no_course = True
        if no_course:
            student_list.append(st)
    return student_list


def get_students_attended_courses(students_courses, courses_number):
    student_list = []
    [student_list.append(st) for st, cs in students_courses.items() if len(cs) >= courses_number]
    return student_list

    # ----------------------------------
    # """Задание 2"""


def get_successful_student(student_group):
    successful_student = {}
    medium_mark = 0
    for student, mark in student_group.items():
        temp_sum = 0
        for i, m in enumerate(mark):
            temp_sum += int(m)
        res = float(temp_sum / len(mark))
        if res >= medium_mark:
            medium_mark = res
            successful_student = student
    print(f'Medium mark is: {medium_mark}')
    return successful_student


def get_non_successful_student(student_group):
    non_successful_student = {}
    medium_mark = 5
    for student, mark in student_group.items():
        temp_sum = 0
        for i, m in enumerate(mark):
            temp_sum += int(m)
        res = float(temp_sum / len(mark))
        if res <= medium_mark:
            medium_mark = res
            non_successful_student = student
    print(f'Medium mark is: {medium_mark}')
    return non_successful_student

    # ----------------------------------
    # """Задание 1"""


# ----------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # ----------------------------------
    """Задание 3
    Написать функцию перевода размеров женского белья из международного во все остальные. 
    Внтри функции нужно просто обращаться к правильно составленному словарю.
    """

    countries = ('International', 'Russia', 'Germany', 'USA', 'France', 'UK', 'obh talii', 'obh beder')

    sizes = []

    int_sizes = ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXL')
    rus_sizes = ('42', '44', '46', '48', '50', '52', '54', '56')
    ger_sizes = ('36', '38', '40', '42', '44', '46', '48', '50')
    usa_sizes = ('8', '10', '12', '14', '16', '18', '20', '22')
    fra_sizes = ('38', '40', '42', '44', '46', '48', '50', '52')
    uk_sizes = ('24', '26', '28', '30', '32', '34', '36', '38')
    tal_sizes = ('63-65', '66-69', '70-74', '75-78', '79-83', '84-89', '90-94', '95-97')
    bed_sizes = ('89-92', '93-96', '97-101', '102-104', '105-108', '109-112', '113-117', '118-122')
    sizes.append(int_sizes)
    sizes.append(rus_sizes)
    sizes.append(ger_sizes)
    sizes.append(usa_sizes)
    sizes.append(fra_sizes)
    sizes.append(uk_sizes)
    sizes.append(tal_sizes)
    sizes.append(bed_sizes)

    size_dict = dict(zip(countries, sizes))

    international_size = 'XS'
    sizes = all_sizes_from_international(size_dict, international_size)
    print(sizes)



    # ----------------------------------
    """Задание 2
    Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, 
    чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). 
    Студент может учиться в нескольких группах. 
    Затем вывести:
    - студентов, которые учатся в двух и более группах
    - студентов, которые не учатся на фронтенде
    - студентов, которые изучают Python или Java
    """
    # courses_dict = {'p': 'Python', 'fr': 'FrontEnd', 'f': 'FullStack', 'j': 'Java'}
    # students = ('Ivan Petrov', 'Peter Ivanov', 'Vasiliy Sidorov', 'Nikolai Valiiev', 'Yegor Yegorov', 'Denys Denisov')
    # courses = (['p', 'fr'], ['f', 'j'], ['p', 'fr', 'f', 'j'], ['fr'], ['p'], ['j'])
    # students_on_courses = dict(zip(students, courses))
    #
    # number = 2
    # students_attend_two_plus = get_students_attended_courses(students_on_courses, number)
    # print(f'The following students attend {number} or more courses: ')
    # print([f'student: {st}' for st in students_attend_two_plus])
    #
    # not_attended_courses = ['fr', 'j']
    # students_without_courses = get_students_without(students_on_courses, not_attended_courses)
    # print('The following students dont attend the courses: ' + str([{courses_dict[c]} for c in not_attended_courses]))
    # print([f'student: {st}' for st in students_without_courses])
    #
    # attended_courses = ['p', 'j']
    # students_with_courses_or = get_students_with(students_on_courses, attended_courses)
    # print('The following students attend courses: ' + str([{courses_dict[c]} for c in attended_courses]))
    # print([f'student: {st}' for st in students_with_courses_or])
    #
    # # ----------------------------------
    # """Задание 1
    # Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
    # Найти самого успешного и самого отстающего по среднему баллу.
    # """
    #
    # # students = ('Ivan Petrov', 'Peter Ivanov', 'Vasiliy Sidorov', 'Nikolai Valiiev', 'Yegor Yegorov', 'Denys Denisov')
    # # marks = ([5, 4, 5, 5, 4, 5], [4, 4, 4, 4, 5, 5, 4, 5], [3, 2, 5, 3, 5, 4], [3, 3, 4, 3], [5, 4], [3, 2, 4, 3, 5])
    # # group = dict(zip(students, marks))
    # # print(f'The best student is: {get_successful_student(group)}')
    # # print(f'The worst student is: {get_non_successful_student(group)}')

