def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples


a = program1([1, 2, 3, 4, 5])
print(a)
print(len(a))

# worse case 3n2+n+2
