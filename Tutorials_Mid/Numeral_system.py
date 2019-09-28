# Intro to number system

# Binary number
1101  # eqiuvalent to
num = 1 * (2**3) + 1 * (2**2) + 0 * (2**1) + 1 * (2**0)
print(num)  # 13
print('-------------------------')
# normally, there is prefix for binary number in Python uses '0b'
# As above, 13 is equivalent to 0b1101
# We also can use bin() method to change from 13 to 0b11o1
num_base_2 = bin(13)
print(num_base_2)  # 0b11o1
print('-------------------------')
base_10 = 56
result = ''
while base_10 > 0:
    result += str(base_10 % 2)
    base_10 = base_10 // 2
print(result)  # 000111
