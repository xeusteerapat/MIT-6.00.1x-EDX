x = int(input('Please enter number: '))

high = x
low = 0.00
mid = (high + low) / 2
epsilon = 0.01

while abs(mid**2 - x) >= epsilon:
    num = float(input('Please enter number to guess: '))
    if num**2 > x:
        high = num
        mid = num
        print('Lower bound is:', low)
        print('Higher bound is:', high)
    else:
        low = num
        mid = num
        print('Lower bound is:', low)
        print('Higher bound is:', high)
print('Answer is:', num)
