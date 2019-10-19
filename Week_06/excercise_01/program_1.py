def program1(x):
    total = 0  # +1
    for i in range(1000):  # +1000
        total += i  # +1000
    # +1000 (in the loop)
    while x > 0:  # +1 compare x > 0
        x -= 1
        total += x

    return total  # +1

# for best case, 1+1000+1000+1000+1+1 = 3003
# best case, we don't go in while loop
# for worse case, we have more 2 steps in while loop
# thus, worse case 5n+3003
