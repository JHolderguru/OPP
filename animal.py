class Animal():


    def __init__(self, species_argument, limbs):
        self.species_parameter = species_argument
        self.limbs = limbs

    def eat(self, food):
        return 'NOM, nom, nom' + food.lower()

    def sleep(self):
        return 'zzzZZZzzzz zzzZZ'

    def potty(self):
        return 'UHHHH ! UUHH !! AHHH !!...o.o '

    def reproduce(self, partner):
        return f'offspring of {self} and {partner}'

# create animal instance
# animal_1 = Animal()
#
# print(animal_1)
# print(animal_1.eat('KFC'))
