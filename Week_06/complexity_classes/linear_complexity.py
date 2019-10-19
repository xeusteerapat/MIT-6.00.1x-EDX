def add_digits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

# O(len(s))


def fact_iter(n):
    products = 1
    for i in range(1, n+1):
        products *= i
    return products

# recursive function still O(n) because
# function calls in linear of n


def fact_recurs(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recurs(n - 1)
