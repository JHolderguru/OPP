from Student_monster import *
from course import *


class Monster_skillset(Student, Course):

    def __init__(self, name='', tax_number=123456, fur=''):
        super().__init__(self, name)
        self.tax_number = tax_number
        self.fur = fur
        self.fur = 'Luxurious black and grey'

    def student_to_course(self, course):
        return 'Well done You have another skill' + course
