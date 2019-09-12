# lists are an ordered sequence of information, accessible by index
# using square brackets, []
# list index is int
# a list contains elements
# usually homogeneous (i.e., all ints)
# can contains mixed types
# lists are mutable

a = []  # empty list
b = [2, 'a', 4, True]
L = [2, 1, 3]

len(L)  # will get 3
L[0]  # indexing to get 2
J = L[2] + 1  # will 4

# lists are mutable
L[1] = 5  # will get [2, 5, 3]

# we can iterate over list, list elements start from 0
# range(n) goes from 0 to n-1
# example, compute sum
A = [1, 2, 3]
total = 0
for i in range(len(A)):
    total += A[i]
print(total)

# but this way is more cleanable
total2 = 0
for i in A:
    total2 += i  # i is integer
print(total2)
