# example tuples, an ordered sequence of elements
a = (1, 2, 'a', 3, 'b')

# indexing
print(a[1])

# concatenate
b = a + (5, 6)
print(b)

# index slicing
print(b[1:3])  # (2, 'a')

# tuples is immutable, you cannot change value of element
# a[0] = 4, will get error

# swap variables with tuple


def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)


(qoute, rem) = quotient_and_remainder(4, 5)
