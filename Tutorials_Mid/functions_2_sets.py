# we can call function with 2 sets of parentheses


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def determine_add_multiply(a):
    if a > 5:
        return add
    else:
        return multiply

# as above, we still not call function inside the if-statement


answer = determine_add_multiply(6)(5, 10)  # we called here
print(answer)  # 15
