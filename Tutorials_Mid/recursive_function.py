# Recursive function is a function that calls itself.

# Factorial recursion


def factorial(n):
    print('New fucntion call. n is:', n)
    if n == 0 or n == 1:
        print('----> Inside first condition')
        return 1  # this is call 'base case'
    else:
        print('----> Inside else condition')
        return n * factorial(n - 1)


answer = factorial(6)
print(answer)

"""
Answer look like below...

New fucntion call. n is: 6
----> Inside else condition
New fucntion call. n is: 5
----> Inside else condition
New fucntion call. n is: 4
----> Inside else condition
New fucntion call. n is: 3
----> Inside else condition
New fucntion call. n is: 2
----> Inside else condition
New fucntion call. n is: 1
----> Inside first condition
720
"""
