from random import randint
number_test = ""
for item in range(10):
    number_test += str(randint(1, 9))
print(type(number_test))
