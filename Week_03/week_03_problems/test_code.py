def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in
    lettersGuessed;
      False otherwise
    '''
    letter_str = ''.join(lettersGuessed)
    temp = []
    for i in secretWord:
        temp.append(letter_str.find(i))
    if -1 not in temp:
        return True
    else:
        return False


secretWord = 'apple'
lettersGuessed = ['a', 'e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed('durian', ['h', 'a', 'c',
                               'd', 'i', 'm', 'n', 'r', 't', 'u']))
