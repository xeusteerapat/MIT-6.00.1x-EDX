try:
    a = 2 / 0
    print(a)
except ZeroDivisionError:
    print('You cannot divide by zero.')
