def fib(n):
    a, b = 0, 1
    list_fib = []
    for i in range(n + 1):
        a, b = b, a + b
        list_fib.append(a)
    return sum(list_fib) * 4


print(fib(100))
