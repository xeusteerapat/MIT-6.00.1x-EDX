import string

shift = 21
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


test_text = 'we are taking 6.00.1x'
#
answer = ''
for i in test_text:
    try:
        answer += mapping_dict[i]
    except KeyError:
        answer += i

print(answer)
