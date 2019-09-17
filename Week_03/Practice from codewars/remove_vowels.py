def disemvowel(string):
    vowels = 'aeiouAEIOU'
    for i in vowels:
        if i in string:
            string = string.replace(i, '')
    return string


print(disemvowel("This website is for losers LOL!"))
