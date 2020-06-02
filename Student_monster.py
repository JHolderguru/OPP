class Student():

    def __init__(self, name='BOO', student_number = '0', skill_list=None):
        if skill_list is None:
            skill_list = []
        self.name = name
        self.student_number = student_number
        self.skill_list = skill_list

    def get_name(self):
        return self.name

    def student_skill_list(self):
        return f'{self.name}This is your newest skillset!'+ self.student_number

    def add_skill(self, skill):
        self.skill_list.append(skill)
        return f'Well done you have another skill'

    def get_skill(self):
        return self.skill_list




