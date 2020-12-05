print('Please, enter three numbers:')
fizzNumber = int(input('Enter first number!'))
buzzNumber = int(input('Enter second number!'))
thirdNumber = int(input('Enter first number!'))

for num in range(1, thirdNumber + 1):
    if num % fizzNumber == 0 and num % buzzNumber == 0:
        print('FB')
    elif num % fizzNumber == 0:
        print('F')
    elif num % buzzNumber == 0:
        print('B')
    else:
        print(num)