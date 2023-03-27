for i in range(10):
    a = 10 - i
    b = i
    print(" " * a, end='')
    for k in range(b):
        print('*', end=' ')
    print()

for i in range(10):
    b = 10 - i
    a = i
    print(" " * a, end='')
    for k in range(b):
        print('*', end=' ')
    print()
