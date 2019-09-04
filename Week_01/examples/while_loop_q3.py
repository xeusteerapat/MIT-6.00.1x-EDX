end = 6
num = 0
while end > 0:
    num += end
    end -= 1
print(num)


# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print(total)
