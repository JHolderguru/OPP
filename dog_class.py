# Abstract and create the class dog
#
from animal import *


# from cat_class import *

class Dog(Animal):


    # this is a special method
    # it comes defined either was but we can re-write it
    # this methods stands for initialize class object  AKA the constructor
    # in other languages

    # Allows us to set a attribute to Dog Objects
    # ...Like the poor thos doestn even have a name  :(
    # we should give it name ...possibly MAx.

    def __init__(self, name='Mad Max', age=0):
        # setting attribute name to instances of Dog class
        self.name = name
        # encapsulate age and make it private
        self.__age_dog = age
        self.__human_age = 0
        self.paws = 4
        self.fur = 'Luxurious black and grey'

    # this is a method that can be used by a Dog instance
    def bark(self, person=''):
        return 'woof, woof!, I see you there' + person

    def eat(self, food):
        return 'NOM, nom, nom' + food.lower()

    def sleep(self):
        return 'zzzZZZzzzz zzzZZ'

    def potty(self):
        return 'UHHHH ! UUHH !! AHHH !!...o.o '

    def getter_age(self):
        return self.__age_dog

        # This print should not be here

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        return True

    def __increase__and__humanyears_(self):
        self.__human_age += 1
        self.__age_dog += 7

    def dog_birthday_incrementer(self):
        # complex block
        #  celebrate the dog's birthday
        print(f' happy birthday Dog! Good Boy {self.name}!')
        # update human year
        self.__human_age += 1
        # update dog years
        self.__age_dog += 7
        return f'dog years at{self.__age_dog} and human years{self.__human_age}'


ringo = Dog(name='Ringo')
print(ringo.name)
# print ringo.name age not longer accessible because it's encapsulated

print(ringo.getter_age())
ringo.dog_birthday_incrementer()
print(ringo.getter_age())
ringo.dog_birthday_incrementer()
print(ringo.getter_age())
# or in this file you define the class dog and add attributes and methods to th class.
# That is it

# print ('woof woof' ) << should not be here
