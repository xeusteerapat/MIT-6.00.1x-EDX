# concatenation
L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # will get [2, 1, 3, 4, 5, 6]

# list method
L1.append(5)  # will get [2, 1, 3, 5]

# extend with more lists
L1.extend([7, 8])  # will get [2, 1, 3, 5, 7, 8]

# remove elements from list
# delete specific index with del(L[index])
del(L1[-1])  # 8 will remove

# remove elements at end of list with L.pop()
L1.pop()  # now 7 will remove

# remove specific element with L.remove(element)
L1.remove(5)
print(L1)
