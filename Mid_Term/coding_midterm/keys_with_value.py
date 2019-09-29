def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    answer = []
    for i, v in aDict.items():
        if v == target:
            answer.append(i)
    return sorted(answer)


print(keysWithValue({0: 0, 8: 2, 10: 0, 6: 2, 7: 0}, 0))
