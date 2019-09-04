s = 'azcbobobegghakl'
current_str = ''
longest_str = ''

for i in range(len(s)):
    if s[i] >= s[i-1]:
        current_str += s[i]
    else:
        current_str = s[i]
    if len(current_str) > len(longest_str):
        longest_str = current_str
print('Longest substring in alphabetical order is:', longest_str)
