x = 27
epsilon = 0.0001
num_guesses = 0
low = 1.0
high = x
answer = (high + low) / 2.0

while abs(answer**3 - x) >= epsilon:
    print('low = ' + str(low) + ', high = ' +
          str(high) + ', answer = ' + str(answer))
    num_guesses += 1
    if answer**3 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print('number of guesses = ' + str(num_guesses))
print(str(answer) + ' is close to square root of ' + str(x))
