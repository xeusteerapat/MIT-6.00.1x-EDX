class Coordinate(object):
    # Create an instance of object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - object) ** 2
        y_diff_sq = (self.y - object) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(origin.x)
