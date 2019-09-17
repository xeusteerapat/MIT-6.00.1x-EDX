# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/Xeus/my-project/MIT-Python-6.001x/Week_03/" \
    "week_03_problems/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp = []
    for i in secretWord:
        if i not in lettersGuessed:
            temp.append('_ ')
        else:
            temp.append(i)
    answer = ''.join(temp)
    return answer


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_str = string.ascii_lowercase
    temp_list = []
    for i in all_str:
        if i not in lettersGuessed:
            temp_list.append(i)
    answer = ''.join(temp_list)
    return answer


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long.')
    print('-------------')
    total_guesses = 8
    mistakesMade = 0
    lettersGuessed = []
    while (total_guesses - mistakesMade) > 0:
        print('You have ' + str(total_guesses - mistakesMade) +
              ' guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:', availableLetters)
        input_letter = input('Please guess a letter: ').lower()
        show_letter = getGuessedWord(secretWord, lettersGuessed)

        if input_letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", show_letter)
            print('-------------')
        elif input_letter in secretWord:
            lettersGuessed.append(input_letter)
            show_letter = getGuessedWord(secretWord, lettersGuessed)
            print('Good guess:', show_letter)
            print('-------------')
        else:
            mistakesMade += 1
            lettersGuessed.append(input_letter)
            show_letter = getGuessedWord(secretWord, lettersGuessed)
            print('Oops! That letter is not in my word:', show_letter)
            print('-------------')

        check_letter = isWordGuessed(secretWord, lettersGuessed)
        if check_letter:
            break

    if (total_guesses - mistakesMade) > 0:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was else. ')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
# secretWord = 'lodge'
hangman(secretWord)
