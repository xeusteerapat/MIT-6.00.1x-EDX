x = int(input('Please think of a number between 0 and 100!'))
epsilon = 0
guess_range = 0
high = x
low =
answer = (high + low) / 2

print("Is your secret number 50?")
print("Enter 'h' to indicate the guess is too high.", end=' ')
print("Enter 'l' to indicate the guess is too low.", end=' ')
print("Enter 'c' to indicate to indicate I guessed correctly.", end=' ')


while abs(answer - x) >= epsilon:
    checking = input()
    if checking not in 'hlc':
        print('Sorry, I did not understand your input.')
    if checking == 'h':
        low = mid
        guess_range = (high - low) / 2
        checking_range = guess_range + low
        print('Is your secret number ', str(checking_range), '?')
    if checking == 'l':
        high = mid
