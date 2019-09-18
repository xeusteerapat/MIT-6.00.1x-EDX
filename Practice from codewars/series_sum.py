def series_sum(n):
    if n == 0:
        return "0.00"
    if n == 1:
        return "1.00"
    sum_num = 0
    for i in range(n-1):
        sum_num = sum_num + (1 / ((2 * (i + 2)) + i))
    answer = 1 + round(sum_num, 2)
    return "{0:.2f}".format(answer)


print(series_sum(5))
