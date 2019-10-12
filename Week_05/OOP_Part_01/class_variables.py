class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return 'animal: ' + str(self.name) + " : " + str(self.age)

# sub-class with class variable


class Rabbit(Animal):
    tag = 1  # class variable

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbit_id = Rabbit.tag  # instance variable
        Rabbit.tag += 1

    def get_rabbit_id(self):
        return str(self.rabbit_id).zfill(3)  # fill with 00

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        # returning of same type as this class
        # recall Rabbit init method
        return Rabbit(0, self, other)

    # method to check if they have same parent
    def __eq__(self, other):
        parents_same = self.parent1.rabbit_id == other.parent1.rabbit_id \
            and self.parent2.rabbit_id == other.parent2.rabbit_id
        parents_opposite = self.parent2.rabbit_id == other.parent1.rabbit_id \
            and self.parent1.rabbit_id == other.parent2.rabbit_id
        return parents_same or parents_opposite


peter = Rabbit(2)
peter.set_name("Peter")

hopsy = Rabbit(3)
hopsy.set_name("Hopsy")
cotton = Rabbit(1, peter, hopsy)  # passing parent argu
cotton.set_name("Cottontail")

print(cotton)
print(cotton.get_parent1())

# example using add method
mopsy = peter + hopsy
mopsy.set_name("Mopsy")
print(mopsy)
print(mopsy.get_parent1())
print(mopsy.get_parent2())

print(mopsy == cotton)  # True
