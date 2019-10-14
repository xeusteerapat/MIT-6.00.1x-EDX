import string
from ps6 import *

shift = 3
lower = string.ascii_lowercase
upper = string.ascii_uppercase
lower_shift = lower[shift:] + lower[:shift]
upper_shift = upper[shift:] + upper[:shift]


upper_list = [x for x in upper]
upper_shift_list = [x for x in upper_shift]
lower_list = [x for x in lower]
lower_shift_list = [x for x in lower_shift]

pair_dict_upper = dict(zip(upper_list, upper_shift))
pair_dict_lower = dict(zip(lower_list, lower_shift_list))
mapping_dict = {}
mapping_dict.update(pair_dict_lower)
mapping_dict.update(pair_dict_upper)


test_text = 'vitalizing'
#


def encrypt_text(shift):
    answer = ''
    for i in test_text:
        try:
            answer += mapping_dict[i]
        except KeyError:
            answer += i
    return answer


print(encrypt_text(shift))
# encrypted = ylwdolclqj with shift = 3
word_list = load_words(WORDLIST_FILENAME)
sample_words = ['vitalizing', 'vitrifying', 'viviparity', 'viviparous']

check = []

for i in sample_words:
    a = ''
    for j in i:
        try:
            a += mapping_dict[j]
        except KeyError:
            a += j
    check.append(a)
print(check)
# if answer in word_list:
#     print('yes')
# else:
#     print('no')

encrypt_text = 'ylwdolclqj'
print(encrypt_text in check)
