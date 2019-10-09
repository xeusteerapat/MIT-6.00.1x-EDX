class House(object):
    # create constructor
    def __init__(self, street, rooms, bathrooms):
        self.street = street
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.clean = True

    # define method
    def cleanHouse(self):
        if not self.clean:
            self.clean = True
            print('This house is now clean.')
        else:
            print('This house is already clean.')

    def unCleanHouse(self):
        if self.clean:
            self.clean = False
            print('This house is now dirty')
        else:
            print('This house was dirty already')

    def talk(self, phrase):
        print(phrase)


house1 = House(35, 15, 16)
print(house1.street)  # 35
print(house1.clean)  # True
print(house1)  # <__main__.House object at 0x10170d128>
