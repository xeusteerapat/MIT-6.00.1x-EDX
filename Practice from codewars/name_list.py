# return values of dictionaries by concatenating with &
def namelist(names):
    temp = []
    for i in range(len(names)):
        temp.append(names[i]['name'])
    if len(temp) == 0:
        return ''
    if len(temp) == 1:
        return ''.join(temp)
    if len(temp) == 2:
        return ' & '.join(temp)
    else:
        last_2 = ', ' + temp[-2] + ' & ' + temp[-1]
        first = temp[:-2]
        return ', '.join(first) + last_2


print(namelist([
    {'name': 'Bart'},
    {'name': 'Lisa'},
    {'name': 'Maggie'},
    {'name': 'Homer'},
    {'name': 'Marge'}]))
