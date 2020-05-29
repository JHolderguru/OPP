#Abstract and create the class dog



class Dog():

    #this is a special method
    #it comes defined either was but we can re-write it
    #this methods stands for initialize class object  AKA the constructor
    # in other languages

    #Allows us to set a attribute to Dog Objects
    #...Like the poor thos doestn even have a name  :(
        # we should give it name ...possibly MAx.


    def __init__(self, name ='Mad Max'):
        # refers to the instance of the object
        self.name = name
        self.age = 17
        self.paws = 4
        self.fur = 'Luxurious black and grey'

    #this is a method that can be used by a Dog instance
    def bark(self, person = ''):
        return 'woof, woof!, I see you there' + person

    def eat(self, food):
        return 'NOM, nom, nom' + food.lower()

    def sleep(self):
        return 'zzzZZZzzzz zzzZZ'

    def potty(self):
        return 'UHHHH ! UUHH !! AHHH !!...o.o '



# This print should not be here
# or in this file you define the class dog and add attributes and methods to th class.
#That is it

#print ('woof woof' ) << should not be here