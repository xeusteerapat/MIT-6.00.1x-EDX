s = 'azcbobobegghakl'
s1 = 'ba'
new_str = ''
list_str = []
for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        new_str += s[i:i+2]
        list_str.append(new_str)
    else:
        print(s[i])
print(new_str)
print(list_str)
