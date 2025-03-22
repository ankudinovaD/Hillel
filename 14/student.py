from human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", {self.record_book}"

    def __eq__(self, student):
        return str(self) == str(student)

    def __hash__(self):
        return hash(str(self))