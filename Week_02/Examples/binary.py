num = 11
# check whether num is negative number or not
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if isNeg:
    result = '-' + result

print(result)
