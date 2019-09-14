def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]


def abs_num(a):
    return abs(a)


print(applyToEach(testList, abs_num))
