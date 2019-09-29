def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    answer = []
    num = int(num)
    for i in range(num):
        diff = abs((base**i) - num)
        answer.append(diff)
    return answer.index(min(answer))


print(closest_power(3, 12))
print(closest_power(4, 12))
print(closest_power(4, 1))
print(closest_power(2, 192.0))
print(closest_power(5, 375.0))
print(closest_power(20, 210.0))
print(closest_power(4, 160.0))
