animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
# print(animals)


def how_many(aDict):
    temp = []
    sub_list = []
    for i in aDict:
        temp.append(aDict[i])
    for j in temp:
        sub_list.append(j)
    answer = sum(sub_list, [])
    return len(answer)


print(how_many(animals))

# MIT answer


def how_many2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result


def how_many3(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result
