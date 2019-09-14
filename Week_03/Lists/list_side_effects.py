# be careful when you're about to mutating a list
warm = ['red', 'yellow', 'orange']
hot = warm
# this is not a good way to do, if you change hot, warm also change
hot.append('pink')
# hot = ['red', 'yellow', 'orange', 'pink']
# warm = ['red', 'yellow', 'orange', 'pink']

# so let's copy and declare to new variable
cool = ['blue', 'green', 'grey']
chill = cool[:]  # better

# avoid mutating a list when you're iterating over a list


def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

remove_dups(L1, L2)
print(L1)  # will get [2, 3, 4] instead of [3, 4]
# because L1 is mutated in the loop

#  do this


def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

remove_dups_new(L1, L2)
print(L1)
