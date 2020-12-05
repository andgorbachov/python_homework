#Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку,
# берете из нее числа, считаете для них fizzbuzz, выводите.

import sys

output = []
f = open('fizzbuzz.py', 'r')
for i, line in enumerate(f):
    my_list = [int(x) for x in line.split(',') if x.strip().isdigit()]
    fizzNumber = my_list[0]
    buzzNumber = my_list[1]
    thirdNumber = my_list[2]

    output_inner = []
    for num in range(1, thirdNumber + 1):
        if num % fizzNumber == 0 and num % buzzNumber == 0:
            output_inner.append('FB ')
        elif num % fizzNumber == 0:
            output_inner.append('F ')
        elif num % buzzNumber == 0:
            output_inner.append('B ')
        else:
            output_inner.append(f'{num} ')
    print(output_inner)
    output.append(output_inner)
f.close()

f = open('fizzbuzz_created.py', 'w+')
f.write('')
for line in output:
    f.write(f'{str(line)}\n')
f.close()