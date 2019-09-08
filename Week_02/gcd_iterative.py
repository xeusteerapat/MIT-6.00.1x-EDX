def gcdIter(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
