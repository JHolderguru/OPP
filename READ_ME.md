#Creating  Monster university Inc

##1.Create all the files- Monster, Student_monster, Course, READ ME 



##2.Sudo Code what you need to do
####Add a new skill to student user
####Create a course with module name and start date
####Be able to add a new student to the course



##3.Define Classes and ##Create some object
```python
   class Student():

    def __init__(self, name='BOO', student_number=654321, skill_list='Change colour of skin'):
        self.name = name
        self.student_number = student_number
        self.skill_list = skill_list

    def get_name(self):
        return self.name

    def student_skill_list(self):
        return 'This is the newest skillset!'



# Another Class
class Monster():

    def __init__(self, name = '',  tax_number=0, fur=''):
        self.name = 'Sullivan'
        self.tax_number = 123456
        self.fur = 'Fluffy and blue'
        
# Another Class
class Course():

    def __init__(self, module_name ='Coool tricks', list_of_students='', start_date='01/01/2021'):
        self.module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date
        self.module2()

    def module_name(self):
        return self.module_name

    def module2(self, scarestyle='Make Eyes PoP'):
        return 'BOBOOOoooHOOOOOO' + scarestyle

    def module3(self):
        return 'The Act of Disappearing'

    def module4(self):
        return 'ZOMBIFY yourself using blue powder'

```
##5.Call some methods and print

### TDD style