x = int(input('Please think of a number between 0 and 100!'))
epsilon = 0
answer = 0
guess_range = 0


print("Is your secret number 50?")
print("Enter 'h' to indicate the guess is too high.", end=' ')
print("Enter 'l' to indicate the guess is too low.", end=' ')
print("Enter 'c' to indicate to indicate I guessed correctly.", end=' ')
checking = input()
if checking not in 'hlc':
    print('Sorry, I did not understand your input.')
if checking == 'h':
    print('Checking is', checking)
if checking == 'l':
    print('Checking is', checking)
if checking == 'c':
    print('Game over. Your secret number was:', answer)

print(type(checking))
