animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

# adding new entry
animals['d'] = 'donkey'
animals.keys()  # to get all keys
animals.values()  # to get all values

# access to values
animals['a']  # will get 'aardvark'

# mutate value in the same key
animals['a'] = 'anteater'

# test if key in dict
'a' in animals  # will return True

# check if values in dict
'donkey' in animals.values()  # return True

# delete entry
del(animals['c'])  # 'c': 'coati' will be deleted
