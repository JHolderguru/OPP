class Student():

    def __init__(self, name='BOO', student_number = '0', skill_list='Change colour of skin'):
        self.name = name
        self.student_number = student_number
        self.skill_list = skill_list

    def get_name(self):
        return self.name

    def student_skill_list(self):
        return f'{self.name}This is your newest skillset!'+ self.student_number




