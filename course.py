class Course():

    def __init__(self, module_name ='Coool tricks', list_of_students=None, start_date='01/01/2021'):
        if list_of_students is None:
            list_of_students = []
        self.module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date

    def add_student(self, student):
        self.list_of_students.append(student)
        return 'Student added'

    def get_list(self):
        students = []
        for s in self.list_of_students:
            students.append(s.get_name())
        return students


    def module_name(self):
        return self.module_name

    def module2(self, scarestyle='Make Eyes PoP'):
        return 'BOBOOOoooHOOOOOO' + scarestyle

    def module3(self):
        return 'The Act of Disappearing'

    def module4(self):
        return 'ZOMBIFY yourself using blue powder'

