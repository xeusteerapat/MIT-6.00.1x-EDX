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


class MITPerson(Person):
    # class variable
    next_id_num = 0

    def __init__(self, name):
        # using init method from parent class
        Person.__init__(self, name)
        self.id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    def get_id_num(self):
        return self.id_num

    def __lt__(self, other):
        return self.id_num < other.id_num

    def speak(self, utterance):
        return (self.get_lastname() + ' says: ' + utterance)


m3 = MITPerson("Mark Zuckerburg")
Person.set_birthday(m3, 5, 14, 84)

m2 = MITPerson("Drew Houston")
Person.set_birthday(m2, 3, 14, 83)

m1 = MITPerson("Bill Gates")
Person.set_birthday(m1, 10, 28, 55)

MITPerson_list = [m1, m2, m3]

print(m3)
print(m3.speak("I'm invester"))

# Create Undergraduate MIT class which is inherit from MITPerson


class UG(MITPerson):
    def __init__(self, name, classYear):
        # using MITPerson init method
        MITPerson.__init__(self, name)
        self.year = classYear

    def get_class(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

# Create class Grad which is inherit from MITPerson


class Grad(MITPerson):
    pass


def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)


s1 = UG("Matt Damon", 2017)
s2 = UG("Ben Affleck", 2017)
s3 = UG("Lin Miranda", 2018)
s4 = Grad("Leonardo Di Carpio")

student_list = [s1, s2, s3, s4]
