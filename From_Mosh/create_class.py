class Point:
    def draw(self):
        print('draw')


point = Point()  # create an instance of object
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))  # check if instance of the class
# return True
