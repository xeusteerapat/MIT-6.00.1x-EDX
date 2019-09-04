s = 'azcbobobegghakl'

num_vowels = 0
for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' \
            or vowel == 'u':
        num_vowels += 1
print("Number of vowels: " + str(num_vowels))
