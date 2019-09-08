# iterative way to greastest common divisor


def gcdIter(a, b):
    list_a = []
    list_b = []
    for i in range(1, a + 1):
        if a % (i) == 0:
            list_a.append(i)
    for i in range(1, b + 1):
        if b % (i) == 0:
            list_b.append(i)
    gcd = max([x for x in list_a if x in list_b])
    return gcd


print(gcdIter(9, 12))
