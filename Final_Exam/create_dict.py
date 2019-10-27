class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.elements = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.elements = [v for v in self.elements if v[0] != key]
        self.elements.append((k, v))

    def getval(self, k):
        """ k, immutable object  """
        return [v[1] for v in self.elements if v[0] == k][0]

    def delete(self, k):
        """ k, immutable object """


md = myDict()
md.assign(1, 2)
print(md)
