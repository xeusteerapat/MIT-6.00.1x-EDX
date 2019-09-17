def fib_efficient(n, d):
    """
    n = number of fibonacci that want to calculate
    d = base case dictionanries
    """
    if n in d:
        return d[n]
    else:
        answer = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = answer
        return answer


# base case
d = {1: 1, 2: 2}  # fib(1) = 1, fib(2) = 2
print(fib_efficient(8, d))
