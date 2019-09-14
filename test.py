def to_camel_case(text):
    new_text = ''
    if text == '':
        return ''
    if '_' in text:
        new_text = text.split('_')
        temp_text = []
        for i in range(len(new_text)-1):
            temp_text.append(new_text[i+1].title())
        return ''.join([new_text[0]] + temp_text)
    if '-' in text:
        new_text2 = text.split('-')
        temp_text2 = []
        for j in new_text2:
            temp_text2.append(j)
        return ''.join(temp_text2)
    else:
        new_text3 = text.split()
        return ''.join(new_text3)


print(to_camel_case('a-catIs-Omoshiroi'))
