def binary_array_to_number(arr):
    sum_num = 0
    n = len(arr)
    for i in range(n):
        n -= 1
        sum_num = sum_num + (arr[i] * (2**n))
    return sum_num


print(binary_array_to_number([1, 0, 1, 0]))
