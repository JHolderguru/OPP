from Student_monster import *
from course import *
from Monster import *


#Be able to add a new student to the course
Test_instance = Student

Enrollment = Student(name='Sullivan', student_number='4321')
print(Enrollment.get_name())
print(Enrollment.student_number)


Enrollment = Student(name='Saskia',student_number='1234')
print(Enrollment.get_name())
print(Enrollment.student_number)

Enrollment = Student(name='Nathan', student_number='4132')
print(Enrollment.name)
print(Enrollment.skill_list)
print(Enrollment.student_number)


#Create a course with module name and start date
Module_n_Date = Course


print(Module_n_Date.module2(''))
module2 = Module_n_Date(start_date='02/01/2021')
print(module2.start_date)

print(Module_n_Date.module3(''))
module3 = Module_n_Date(start_date='09/01/2021')
print(module3.start_date)

module4 = Module_n_Date(start_date='13/01/2021')
print(Module_n_Date.module4(''))
print(module4.start_date)


#Add a new skill to student user
skillset = Monster_skillset
print(skillset.student_to_course(Monster_skillset,'Sullivan', ' module 4'))

skillset = Monster_skillset
print(skillset.student_to_course(Monster_skillset,'Nathan', ' module 2'))
