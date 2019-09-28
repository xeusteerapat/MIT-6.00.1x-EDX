# list comprehensive form
# [<value_to_include> for <elem> in <sequence> if <condition>]

L = [x**2 for x in range(1, 7)]
# will return [1, 4, 9, 16, 25, 36]

# we also can add condition in list comprehension
mixed = [1, 2, 'a', 3, 4.0]

squared_int = [x**2 for x in mixed if type(x) == 'int']
# will return [1, 4, 9]
