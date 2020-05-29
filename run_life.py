# Import classes here and run methods initial objs and run methods

#This separation will maintain your code more organised following speration of concerns


from dog_class import *

#Initializing a Dog object
# dog_instance1 = Dog()
#
# print(dog_instance1)
# print(type(dog_instance1))


max_dog_instance = Dog()
ringo_dog_instance = Dog('Ringo')
#Call the metho .bark() on object

print(max_dog_instance.name)
print(ringo_dog_instance.name)
#
# print(max_dog_instance.eat('bone'))
# print(max_dog_instance.bark)
# print(max_dog_instance.potty)
# print(max_dog_instance.sleep)
#
# print(max_dog_instance.bark(' Creepy Stranger!!'))





