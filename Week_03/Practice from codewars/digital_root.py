def digital_root(n):
    sum_num = 0
    if n <= 99:
        temp = [int(d) for d in str(n)]
        for num in temp:
            sum_num += num
        return sum_num
    else:
        temp = [int(d) for d in str(n)]
        for num in temp:
            sum_num += num
        return digital_root(sum_num)


print(digital_root(456))
