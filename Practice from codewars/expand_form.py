def expanded_form(num):
    temp = list(str(num))
    list_int = [int(x) for x in temp]
    power = len(temp)
    new_list = []
    for i in list_int:
        power -= 1
        new_list.append(i * 10**power)
    answer = [str(x) for x in new_list if x != 0]
    return ' + '.join(answer)


print(expanded_form(134546452))
