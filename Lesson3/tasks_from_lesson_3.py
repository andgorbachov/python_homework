
#------------------------------------------------------------------------------
#Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
output = 0
note1000 = 1000
note500 = 500
note200 = 200
note100 = 100
note50 = 50
note20 = 20
note10 = 10
note5 = 5
note2 = 2
note1 = 1
banknotes = {note1: 0, note2: 0, note5: 0, note10: 0, note20: 0, note50: 0, note100: 0, note200: 0, note500: 0, note1000: 0}
entered_sum = int(input('Enter the desired sum.'))
sum = entered_sum
print(f'Take your money:')
for i, note in enumerate(banknotes):
    while sum - note >= 0:
        if banknotes.get(note) < 10:
            sum -= note
            check = banknotes.get(note)
            banknotes.update({note: banknotes.get(note) + 1})
        else:
            break
        continue
while sum != 0:
    output = 0
    note_to_exclude = sum
    sum = entered_sum
    banknotes = {note1: 0, note2: 0, note5: 0, note10: 0, note20: 0, note50: 0, note100: 0, note200: 0, note500: 0,
                 note1000: 0}
    for i, note in enumerate(banknotes):
        if note == note_to_exclude:
            continue
        while sum - note > 0:
            if banknotes.get(note) < 10:
                sum -= note
                try:
                    check_to_delete = banknotes.get(note)
                    banknotes.update({note: banknotes.get(note) + 1})
                except:
                    break
            else:
                break
            continue
        if sum == note_to_exclude:
            check_to_delete = banknotes.get(sum)
            try:
                banknotes.update({sum: banknotes.get(sum) + 1})
            except:
                break
            sum -= note

    if sum != 0:
        for i, note in enumerate(banknotes):
            while sum - note >= 0:
                if banknotes.get(note) >= 10 and banknotes.get(note) != note1000:
                    break
                sum -= note
                banknotes.update({note: banknotes.get(note) + 1})
                if sum == 0:
                    break
            if sum == 0:
                break
    for i, note in enumerate(banknotes):
        if banknotes.get(note) > 0:
            output += banknotes.get(note) * note
    if output != entered_sum:
        continue

output = 0
for i, note in enumerate(banknotes):
    if banknotes.get(note) > 0:
        print(f'{banknotes.get(note)} x {note} uah')
        output += banknotes.get(note) * note
print(output)


#------------------------------------------------------------------------------

#Банкомат выдает сумму максимально возможными купюрами
# note1000 = 1000
# note500 = 500
# note200 = 200
# note100 = 100
# note50 = 50
# note20 = 20
# note10 = 10
# note5 = 5
# note2 = 2
# note1 = 1
# banknotes = {note1000: 0, note500: 0, note200: 0, note100: 0, note50: 0, note20: 0, note10: 0, note5: 0, note2: 0, note1: 0}
# entered_sum = int(input('Enter the desired sum.'))
# print(f'Take your money:')
# for i, note in enumerate(banknotes):
#     while entered_sum - note >= 0:
#         entered_sum -= note
#         banknotes.update({note: banknotes.get(note) + 1})
#         continue
#     if banknotes.get(note) > 0:
#         print(f'{banknotes.get(note)} x {note} uah')

#------------------------------------------------------------------------------

#Написать программу, которая выводит саму себя задом наперед
# import sys
# filename = sys.argv[0]
# print(sys.argv[0])
# f = open(filename, 'r+')
# tempList = []
# for line in f:
#     tempList.append(line)
# tempList.reverse()
# for i, line in enumerate(tempList):
#     print(line)
#     if i == 10:
#         print("__________That's enough. The end of output.__________")
#         break
# f.close()


#------------------------------------------------------------------------------

#Написать программу, которая выводит сама себя
# Работа с файлом
# import sys
# filename = sys.argv[0]
# print(sys.argv[0])
# f = open(filename, 'r+')
# for i, line in enumerate(f):
#     print(line)
#     if i == 10:
#         print("__________That's enough. The end of output.__________")
#         break
# f.close()


#------------------------------------------------------------------------------


#Каждый пишет сумму списка при помощи for и while
# list = [12, 25, 186, 30, 21]
# sumWhile = sumFor = i = 0
# # While loop
# while i < len(list):
#     sumWhile += list[i]
#     i += 1
# print(sumWhile)
#
# # For loop
# for i in list:
#     sumFor += i
# print(sumFor)


#------------------------------------------------------------------------------

# # enumerate
# c = {1: 'a', 2: 'b', 3: 'c'}
# for i in enumerate(c):
#     print(c[i[1]])