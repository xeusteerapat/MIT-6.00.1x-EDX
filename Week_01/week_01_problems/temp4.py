s = 'hiyoou'

new_string = ""

lst = []
for char in s:
    if char in 'hio':
        new_string += char
        lst.append(new_string)
print(new_string)
print(lst)
