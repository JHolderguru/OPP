#lion call will inherit all the behaviours and characteristic
from random import random

from animal import *

# #create animal instance
# animal_1 = Animal()
#
# print(animal_1)
# print(animal_1.eat('KFC'))


#to inherit pass the entire parent class to your subclass
class Lion(Animal):
    'bla bla'
    #POL MORPHISM _ CALLING ON PARENT METHOD TO KEEP BOTH FUNCTIONALIES

    def __init__(self, name ='TOBY', owner='filipe'):
        super().__init__('Small lion', 3)
        self.name = name
        self.owner = owner
    #     #
# lion_king = Lion()
#
# print(lion_king.eat(' buffalo'))
#print(lion_king.roar())