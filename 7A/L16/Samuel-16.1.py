class Dog(object):

    def __init__(self, name):
        self.name = name
        print("my dog's name: %s" % (self.name))

    def bark(self):
        return self.name + ' is barking!'

my_Dog = Dog('icecream')
print(my_Dog.bark())