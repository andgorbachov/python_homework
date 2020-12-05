from operator import itemgetter

# #----------------------------------
# Задание 3

def update_dict(dictionary, string):
    if dictionary.keys().__contains__(string):
        dictionary.update({string: dictionary.get(string) + 1})
    else:
        dictionary[string] = 1
    return dictionary


# #----------------------------------
# Задание 2

def simple_number(number):
    res = False
    for i in range(1, number):
        if number in range(1, 4) or i == 1:
            res = True
            continue
        elif number % i == 0:
            res = False
            break
    return res


def power_simple_number(number):
    return [number ** 2 if simple_number(number) or number == 1 else '']

# #----------------------------------
# Задание 1

def to_lower(string):
    return string.lower()


def to_upper(string):
    return string.upper()


# #----------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # ----------------------------------
    """Задание 3
    Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. 
    Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
    """

    f = open('WordsToCount.txt', 'r+')
    words = list(map(lambda x: x.strip(',.!?'), f.read().split()))
    f.close()
    counted_words = dict(map(lambda x: (x, words.count(x)), words))
    sorted_desc_dict = sorted(counted_words.items(), key=itemgetter(1), reverse=True)
    print([f'"{key}" met {value} times' for key, value in sorted_desc_dict])


    # ----------------------------------
    """Задание 2
    Написать функцию которая будет простое число возводить в квардрат.
    Необходимо возвести в квадрат все простые числа в списке используя функцию map"""

    digit_list = range(1, 30)
    print(list(digit_list))
    print(list(map(power_simple_number, digit_list)))

# ----------------------------------
    """Задание 1
    Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
    Вторая функция будет принимать строку и проводить ее к верхнему регистру.
    После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!"""

    list_string = ['aaa', 'bbb', 'ccc']
    result = list(map(to_lower, list_string))
    print(result)
    result = list(map(to_upper, list_string))
    print(result)