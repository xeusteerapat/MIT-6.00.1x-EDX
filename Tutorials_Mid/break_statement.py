# with while-loop
num = 5

while True:
    if num > 9:
        print(num)
        break
    print(num)
    num += 1  # increment num by 1 until more than 9 and stop
print(num)
print('-------------------------')

# with for-loop
for i in range(5, 15):
    if i % 2 == 0:
        break
    print(i)
