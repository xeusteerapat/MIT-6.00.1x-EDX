# most polynomial complexity are quadratic
# growth with square of size of input


def is_subset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    """find intersect list"""
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res


b = intersect([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print(b)
