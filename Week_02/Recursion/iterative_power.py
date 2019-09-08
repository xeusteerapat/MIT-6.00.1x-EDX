def iterPower(base, exp):
    if base == 1 or exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        result = 1
        while exp > 0:
            result *= base
            exp -= 1
        return result


print(iterPower(2, 5))
