s = 'hiyou'

for c in s:
    print(c, end=', ')  # this will print h, i, y, o, u,
print('\n')

for i in range(len(s)):
    print(i, s[i], end=', ')  # print index and character
print('\n')

for i, c in enumerate(s):
    print(i, c, end=', ')  # print index and character
