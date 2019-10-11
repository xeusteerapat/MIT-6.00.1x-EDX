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


platoo = Cat(2)
platoo.set_name("Platoo")
print(platoo)
print(platoo.speak())

mojo = Rabbit(3)
mojo.set_name("Mojo")
print(mojo)
print(mojo.speak())

francis = Animal(4)
print(francis.speak())  # error, cannot get method from child class
