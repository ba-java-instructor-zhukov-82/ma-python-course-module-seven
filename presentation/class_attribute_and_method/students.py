class Student:
    # Common base class for all students

    stdCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stdCount += 1

    def display_student(self):
        print("Name : ", self.name, ", Age: ", self.age)

    @staticmethod
    def student_count():
        print("Total Students count %i" % Student.stdCount)
