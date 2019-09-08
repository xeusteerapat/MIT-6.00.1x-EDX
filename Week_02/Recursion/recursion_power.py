def recurPower(base, exp):
    if base == 1 or exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(2, 5))
