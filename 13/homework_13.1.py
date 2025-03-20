class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", {self.record_book}"


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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Name1', 'LastName1', 'AN145')
st3 = Student('Male', 25, 'Name2', 'LastName2', 'AN145')
st4 = Student('Female', 25, 'Name3', 'LastName3', 'AN145')
st5 = Student('Male', 25, 'Name4', 'LastName4', 'AN145')
st6 = Student('Female', 25, 'Name5', 'LastName5', 'AN145')
st7 = Student('Male', 25, 'Name6', 'LastName6', 'AN145')
st8 = Student('Female', 25, 'Name7', 'LastName7', 'AN145')
st9 = Student('Male', 25, 'Name8', 'LastName8', 'AN145')
st10 = Student('Female', 25, 'Name9', 'LastName9', 'AN145')
st11 = Student('Female', 25, 'Name10', 'LastName10', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)

# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
# gr.delete_student('Taylor')  # No error!
