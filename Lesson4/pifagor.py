for i in range(0, 10):
    if not i:
        print('\t', end='')
        [print(x, end='\t') for x in range(1, 10)]
    else:
        print(i, end='\t')
        [print(i*x, end='\t') for x in range(1, 10)]
    print()