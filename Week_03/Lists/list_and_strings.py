# conver string to list use list(string)
s = 'I <3 cs'
print(list(s))  # will get ['I', ' ', '<', '3', ' ', 'c', 's']

# use split method to split string on character
print(s.split('<'))  # return ['I ', '3 cs']

# use ''.join(L) to turn a list of character to string
L = ['a', 'b', 'c']
print(''.join(L))  # return 'abc'
print('_'.join(L))  # reurn 'a_b_c'
