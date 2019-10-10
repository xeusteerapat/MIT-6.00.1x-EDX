def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i]
    """
    ratios = []
    for idx in range(len(L1)):
        try:
            ratios.append(L1[idx] / float(L2[idx]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with wrong arg')
    return ratios


L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = [5, 6, 7]
L4 = [5, 6, 7, 0]

print(get_ratios(L1, L2))
print(get_ratios(L1, L3))  # this case will an error with our message
print(get_ratios(L1, L4))  # last element is nan
