# Import classes here and run methods initial objs and run methods

#This separation will maintain your code more organised following speration of concerns

from dog_class import *

#Initializing a Dog object
dog_instance1 = Dog()
#
print(dog_instance1)
# print(type(dog_instance1))

ringo = Dog(name='Ringo')
# # # print(ringo.name)
max_dog_instance = Dog(name='Max')
#


#Call the method.bark() on object

print(max_dog_instance.name)
# print(ringo_dog_instance.name)
print(ringo.dog_birthday_incrementer())
#
#
# # print(ringo_dog_instance.reproduce)
#
# print(max_dog_instance.eat('bone'))
# print(max_dog_instance.bark)
print(max_dog_instance.potty)


