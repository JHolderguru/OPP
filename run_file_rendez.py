import Student_monster
from Student_monster import *
from course import *
from Monster import *


# Create 2 student objects
enrollment = Student(name='Saskia', student_number='1234')
print(enrollment.get_name())
print(enrollment.student_number)

enrollment1 = Student(name='Nathan', student_number='4132')
print(enrollment1.get_name())
print(enrollment1.student_number)

# Add a skill to each of your student
print(enrollment.add_skill('Scaring 10 year olds'))
print(enrollment.get_skill())

print(enrollment1.add_skill('Scaring 12 year olds'))
print(enrollment1.get_skill())

# Create a course
module_n_date = Course()
print(module_n_date.module2(''))



# Append student object/instances to list student in attribute in one of the courses

module_n_date.add_student(enrollment1)
module_n_date.add_student(enrollment)





# Extra: Get the list of students , iterate over it and print the students name

# students = module_n_date.list_of_students
# for s in students:
#     print(s.get_name())
module_n_date.get_list()
print(module_n_date.get_list())