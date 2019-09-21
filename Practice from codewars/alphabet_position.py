def alphabet_position(text):
    new_text = ''.join(text.split(' '))
    not_char = "'."
    for i in new_text:
        if i in not_char:
            new_text = new_text.replace(i, '')
    new_text = new_text.lower()
    list_text = list(new_text)
    list_nums = [ord(x) - 96 for x in list_text]
    for j in list_nums:
        if j < 0:
            return ""
    nums_to_char = [str(x) for x in list_nums]
    answer = ' '.join(nums_to_char)
    return answer


print(alphabet_position("8197977148"))
