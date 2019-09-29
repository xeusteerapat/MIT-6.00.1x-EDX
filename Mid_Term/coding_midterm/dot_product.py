def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    answer = 0
    for i in range(len(listA)):
        dot = listA[i] * listB[i]
        answer += dot
    return answer


print(dotProduct([1, 2, 3], [4, 5, 6]))
