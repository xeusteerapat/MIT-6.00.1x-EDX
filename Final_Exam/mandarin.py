trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if int(us_num) < 11:
        return trans[us_num]
    elif 11 <= int(us_num) < 20:
        return trans['10'] + ' ' + trans[us_num[1]]
    elif int(us_num) % 10 == 0:
        return trans[us_num[0]] + ' ' + trans['10']
    else:
        return trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]


print(convert_to_mandarin('16'))
print(convert_to_mandarin('99'))
print(convert_to_mandarin('36'))
print(convert_to_mandarin('0'))
