def persistence(n):
    list_int = [int(x) for x in list(str(n))]
    result = 1
    for i in list_int:
        result *= i
    return persistence(result)


print(persistence(39))
