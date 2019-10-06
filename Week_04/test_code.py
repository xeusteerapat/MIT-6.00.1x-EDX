import random
import string

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

path = '/Users/Xeus/my-project/MIT-Python-6.001x/Week_04/PS4/'
WORDLIST_FILENAME = path + "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


chk = {'h': 1, 't': 2, 'u': 2, 'o': 2, 'a': 1, 'y': 1, 'c': 2, 'z': 1}
word = 'chayote'
a = getFrequencyDict(word)
print(chk)
print(a)

for i in a:
    # print(i)
    if i in chk:
        if chk[i] >= a[i]:
            print('yes')
        else:
            print('n')
    else:
        print('no')


# temp_hand = chk.copy()
# for i in word:
#     if i in chk:
#         temp_hand[i] -= 1
# ans = [x for x in temp_hand.values()]
# # for j in temp_hand.values():
# #     ans.append(j)
# print(ans)

# a =
