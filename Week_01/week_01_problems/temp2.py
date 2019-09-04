s = 'hiyoou'

lst = []
for c in s:
    if c in 'yu':
        lst.append(c)
    print(lst, end=', ')
strung_list = "".join(lst)
print("\nstrung_list is ", strung_list)
print("\nand I'll assume you know how to compare the length of")
print(" two lists or strings\n")
print(type(strung_list))
