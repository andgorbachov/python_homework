answer = int(input('Could you please provide us with your income? We will try to guess what are you.'))
if answer <= 2000:
    print('You probably a student! Or you have decided to have a rest')
elif 2000 < answer <= 10000:
    if answer == 5000:
        print('You earn the minimal salary in Ukraine.')
    print('Looks like you can be a nurse in ukrainian hospital or salesman in the store')
elif 10000 < answer < 50000:
    print('You can be any anyone!')
elif answer == 50000:
    print('Are you middle python developer?')
elif 50000 < answer <= 200000:
    print('You definitely can afford travel a lot!')
elif 200000 < answer <= 10000000:
    if answer > 1000000:
        print('You are millionaire!!! Our Congratulations!!!')
    print('Looks like you can make anybody happy spending less than 5 % of your income for the gifts.')
else:
    print('Hello Bill Gates!')