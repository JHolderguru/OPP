# Intro to OOP


what is OOP,
why  OOP.


How to OOP.

###Class
What is a class? A class is like a cookie cutter or blue print for objects but not
the object itself.

what can you do with a cookie 
  -eat it
  
 ### Methods
 the actions or how an object behaves.

So in the above example, eat cookie() could be a method



### Instance

```python
class Dog():
    def __init__(self, attri1, attri2, optional_attri='default'):
        self.attribute_1 = attri1,
        self.attribute_2 = attri2,
        self.attribute_3 = optional_attri,

    def method_name(self, arg1):
        # complex block
        arg1 += arg1 + 1 
        return  arg1 
```

##4 Pillars
###inheritance 
The ability of a subclass to inherit all the behaviour and methos from parent class.
One of the core reasons to use OOP, because it means you write less code.In reality
this is debatable, has you end up




### Abstraction
-good naming
-good documentation
-use of inheritance

####
-what is class polymorphism
-what is method polymorphism

###Encapsulation
The ability to limit from the exterior to method and or attributes
hance making them private
class Dog():
```python
    def __init__(self, dog_name, attri2):
        self.name = attri1,
        self.attribute_2 = attri2,
        self.dog_years = 0,
        self.human_years = 0

    def dog_birthday_incrementer(self):
        # complex block
        #  celebrate the dog's bithday 
        # update human year
        # update dog years
        print(f'happy birthday! You are a GOOD BOY! GOOD BOY {self.name}!')
        return self.dog_years 
```
