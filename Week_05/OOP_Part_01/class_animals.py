import random


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

# Inheritance


class Cat(Animal):
    def speak(self):
        print("Meowwww...")

    # method overriding from parent class
    def __str__(self):
        return 'Cat: ' + str(self.name) + " : " + str(self.age)


class Rabbit(Animal):
    def speak(self):
        print("Meeepp...")

    # method overriding from parent class
    def __str__(self):
        return 'Rabbit: ' + str(self.name) + " : " + str(self.age)


# Create class Person which inherit from Animal
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)  # call Animal constructor
        Animal.set_name(self, name)  # call Animal Method
        self.friends = []  # add new data attribute

    def get_friends(self):
        return self.friends

    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def speak(self):
        print('Hello')

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    # overide Animal's method
    def __str__(self):
        return 'Person: ' + str(self.name) + " : " + str(self.age)


# Create student class which inherit from Person


class Student(Person):
    def __init__(self, name, age, major=None):
        # inherit Person and Animal attributes
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print("I need to slepp")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return 'Student: ' + str(self.name) + " : " + str(self.age) + " : "
        + self.major


platoo = Cat(2)
platoo.set_name("Platoo")
print(platoo)
print(platoo.speak())

mojo = Rabbit(3)
mojo.set_name("Mojo")
print(mojo)
print(mojo.speak())

francis = Animal(4)
# print(francis.speak())  # error, cannot get method from child class

eric = Person('Eric', 45)
teerapat = Person("Teerapat", 33)

print(eric.speak())

print(eric.age_diff(teerapat))

fred = Student('Fred', 18, 'Course VI')
print(fred)
print(fred.speak())
print(fred.speak())
print(fred.speak())
print(fred.speak())
