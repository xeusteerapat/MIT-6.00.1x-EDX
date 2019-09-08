def f(x):
    x = x + 1
    print('in f(x): x = ', x)
    return x


x = 3
z = f(x)
print(x)
# you'll get in f(x): x =  4, but value of x still 3
