from cat_class import *


#Initialize the class
cat_instance = Cat()
print(cat_instance)

# To assign an enemy
fight = cat_instance.fight(' fox')
print(fight)

# To assign the food
food = cat_instance.food(' juicy mice')
print(food)

# To print the Color
print(cat_instance.colour())

#Print the instance
print(cat_instance.name)

#Print another new cat in the area


#def __init__(self, name ='eM Jay',eye_colour='', fur ='', age=0):
new_cat = Cat('Garfield', 'blue', 'black', age=3)
print(new_cat.name)
print(new_cat.eye_colour)
print(new_cat.age)
