def middle_way(a, b):
    answer = [a[1:2], b[1:2]]
    return [x for y in answer for x in y]


print(middle_way([1, 2, 3], [4, 5, 6]))
