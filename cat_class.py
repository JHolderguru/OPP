#Create a class cat

class Cat():

from animal import *

    def __init__(self, name ='eM Jay',eye_colour ='', fur ='', age=0):
        # refers to the instance of the object
        self.name = name
        self.age = int(age)
        self.paws = 4
        self.fur = 'Fluffy grey'
        self.eye_colour = 'Black'
    def type(self):
        return 'I am a street cat, I like the wild! '

    def colour(self):
        return 'Grey with blue eyes '

    def food(self, food):
        return 'Grrrrrrr ,meeeooowww' + food.lower()

    def sleep(self):
        return 'zzzZZZzzzzzZZ '

    def fight(self, enemy):
        return 'GrrrrrrrrRRRrrawww raawwww ' + enemy.lower()

    def coughball(self):
        return 'Hrrrrrrrzzzzzz HHrrrAAAAA '

    def happy(self):
        return 'PrrrRRRRrrrrr Prrrrr '

#polymorphsm - redefining the method
    def reproduce(self):
        return f"amazing feline specimen of {self} "



