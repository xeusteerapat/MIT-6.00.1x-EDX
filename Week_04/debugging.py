def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0  # count to be define before code run tinto while-loop
    while x >= a:
        count += 1
        x = x - a
    return count


print(integerDivision(5, 3))
