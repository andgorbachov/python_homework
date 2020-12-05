# Проверить, является ли введеное число четным.
# number = int(input('Enter the number:'))
# if number % 2 == 0:
#     print(f'Entered number, {number} is Even')
# else:
#     print(f'Entered number, {number} is Odd')

# Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.
# number = int(input('Enter the number:'))
# if number % 2 == 1 and number % 3 == 0 and number % 5 == 0 and number % 10 != 0:
#     print(f'Entered number, {number} is Even AND divide on 3 and 5 AND not divide on 10')
# else:
#     print(f'Entered number, {number} is not satisfied to the condition')

# Ввести число, вывести все его делители.
# number = int(input('Enter the number:'))
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(f'The number {i} id divider of {number}')

# Ввести число, вывести его разряды и их множители.
number = int(input('Enter the number:'))
strNumber = number.__str__()
index = len(strNumber)
print(strNumber)
print(type(strNumber))

for i in strNumber:
    index -= 1
    print(f'{i}*10^{index}')
    
