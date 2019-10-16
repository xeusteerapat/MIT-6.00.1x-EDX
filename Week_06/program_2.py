def program2(x):
    total = 0  # +1
    for i in range(1000):  # +1000, assign value to i
        total = i
    # +1000, for loop
    while x > 0:  # +1, best case not enter loop
        x = x//2
        total += x

    return total  # +1, return value

# best case, 1+1000+1000+1+1 = 2003
# worse case 5log2(n)+2008
