def multiply(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)


print(multiply(0, 1))
