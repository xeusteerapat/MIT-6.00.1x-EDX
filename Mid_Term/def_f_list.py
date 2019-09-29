def f(x):
    print('New fucntion call. n is:', x)
    a = []
    while x > 0:
        a.append(x)
        print('x appended to list')
        f(x-1)


print(f(5))
