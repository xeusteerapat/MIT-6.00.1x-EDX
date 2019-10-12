import datetime


class Person(object):
    def __init__(self, name):
        """crete person called name"""
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def get_lastname(self):
        """return self's lastname"""
        return self.lastname

    def set_birthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def get_age(self):
        """return self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, False otherwise"""
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        """return self's name"""
        return self.name
# example usage


p1 = Person('Mark Zuckerberg')
p1.set_birthday(5, 14, 84)
p2 = Person('Drew Houston')
p2.set_birthday(3, 4, 83)
p3 = Person('Bill Gates')
p3.set_birthday(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

person_list = [p1, p2, p3, p4, p5]
for ele in person_list:
    print(ele)
print('-------------')
person_list.sort()
for ele in person_list:
    print(ele)
