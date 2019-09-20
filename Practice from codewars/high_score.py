def high(x):
    temp = x.split(' ')
    list_char = []
    for i in temp:
        char_int = 0
        for j in i:
            char_int += ord(j) - 96
        list_char.append(char_int)
    answer = [int(x) for x in list_char]
    ind = answer.index(max(answer))
    return temp[ind]


high('man i need a taxi up to ubud')
