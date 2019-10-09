class Coordinate(object):
    # Create an instance of object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    # special method
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    # finding coordinate by subtraction
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)


c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c)  # if you're not define __str__ it will go to garbage collection
print(type(c))  # <class '__main__.Coordinate'>
print(c.x)
print(origin.x)
foo = c - origin
print(foo)  # <3, 4>

# using method
print(c.distance(origin))  # 5.0
print(Coordinate.distance(c, origin))  # 5.0
