print('Please think of a number between 0 and 100!')
num_guesses = 0
low = 0
high = 100
answer = int((high + low) / 2.0)
checking = ''

while checking != 'c':
    answer = int((high + low) / 2.0)
    print("Is your secret number ", answer, '?')
    print("Enter 'h' to indicate the guess is too high.", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    print("Enter 'c' to indicate to indicate I guessed correctly.", end=' ')
    checking = input()
    if checking not in 'hlc':
        print('Sorry, I did not understand your input.')
    if checking == 'h':
        high = answer
        answer = int((high + low) / 2)
    if checking == 'l':
        low = answer
        answer = int((high + low) / 2)
    if checking == 'c':
        break
print('Game over. Your secret number was:', answer)
