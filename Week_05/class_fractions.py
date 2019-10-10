class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    # accessing to attributes
    def get_numer(self):
        return self.numer

    def get_denom(self):
        return self.denom

    # adding more methods, add and subtract
    def __add__(self, other):
        new_numer = other.get_denom() * self.get_numer() \
            + other.get_numer() * self.get_denom()
        new_denom = other.get_denom() * self.get_denom()
        return Fraction(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = other.get_denom() * self.get_numer() \
            - other.get_numer() * self.get_denom()
        new_denom = other.get_denom() * self.get_denom()
        return Fraction(new_numer, new_denom)

    def convert(self):
        return self.get_numer() / self.get_denom()


one_half = Fraction(1, 2)
two_third = Fraction(2, 3)
three_quarters = Fraction(3, 4)
print(one_half)  # 1/2
print(two_third)  # 2/3

print(one_half.get_numer())  # 1
print(two_third.get_denom())  # 3
print(one_half + two_third)  # 7 / 6
print(two_third - three_quarters)  # -1 / 12
print(two_third.convert())  # 0.666667
