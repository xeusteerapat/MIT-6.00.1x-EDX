s = 'azcbobobegghakl'
count = 0
first_index = 0
last_index = 3
for i in s:
    if s[first_index:last_index] == 'bob':
        count += 1
    first_index += 1
    last_index += 1
print(count)
