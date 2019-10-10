class IntSet(object):
    def __init__(self):
        self.vals = []

    # crete insert methods
    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    # check elements in list
    def member(self, e):
        return e in self.vals

    # remove element
    def remove(self, e):
        try:
            self.vals.remove(e)
        except ValueError:
            raise ValueError(str(e) + ' not found')

    # print set of integers
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return "{" + result[:-1] + "}"


s = IntSet()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(2)
print(s)
print(s.member(5))
s.remove(6)
