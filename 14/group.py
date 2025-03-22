class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):

        if len(self.group) >= 10:
            raise ValueError("В групі не може бути більше 10 студентів.")
        self.group.add(student)


    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'