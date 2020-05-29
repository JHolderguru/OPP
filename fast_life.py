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

new_cat = Cat('Garfield')
print(new_cat.name)
