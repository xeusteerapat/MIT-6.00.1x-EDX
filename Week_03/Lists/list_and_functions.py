# we can apply function to each element in a list
def apply_to_each(L, f):
    """
    L = list
    f = function
    mutate L by replacing each element of L by app f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


L = [1, -2, 3.4]

print(apply_to_each(L, abs))

# or use function as element of a list


def apply_func(L, x):
    for f in L:
        print(f(x))


apply_func([abs, int, float], 4)
