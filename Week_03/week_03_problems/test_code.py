import string


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
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    temp = []
    for i in secretWord:
        if i not in lettersGuessed:
            temp.append('_ ')
        else:
            temp.append(i)
    answer = ''.join(temp)
    return answer


# print(getGuessedWord(secretWord, lettersGuessed)
#       )


def getAvailableLetters(lettersGuessed):
    all_str = string.ascii_lowercase
    temp_list = []
    for i in all_str:
        if i not in lettersGuessed:
            temp_list.append(i)
    answer = ''.join(temp_list)
    return answer


# print(
#     getAvailableLetters(lettersGuessed))
