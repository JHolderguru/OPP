from Student_monster import *
from course import *


class Monster_skillset(Student):

    def __init__(self, name, tax_number=123456, fur=''):
        super().__init__(name, tax_number, fur) #self shouldnt be used in the super
        self.tax_number = tax_number
        self.fur = fur


    def student_to_course(self, name, course):
        return f'Well done {name} ,You have another skill' + course
