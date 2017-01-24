from types import MethodType
from presentation.class_attribute_and_method.students import Student
from presentation.class_attribute_and_method.presence import today_presence, no_attr

# This would create first object of Student class
student1 = Student("Anton", 17)

# This would create second object of Student class
student2 = Student("Masha", 18)


student1.display_student()
student2.display_student()

Student.student_count()


# You can add, remove, or modify attributes of classes and
# objects at any time:
# ADD attribute
student1.grade = 4
print('New Student attribute \'grade\' created with value:', student1.grade)
# MODIFY attribute
student1.grade = 5
print('student1 attribute \'grade\' modified to value:', student1.grade)
# DELETE attribute
del student1.grade
try:
    print(student1.grade)
except AttributeError:
    print(AttributeError.__doc__)

# ADDING of a new method
student1.presence = MethodType(today_presence, student1)
student1.presence()
# Pseudo DELETING of a added method
student1.presence = lambda *a, **k: no_attr()
student1.presence()

# ADDING an attribute to all class instances via its name
Student.test = 'test'
print(student1.test)
del Student.test
try:
    print(student1.test)
except AttributeError:
    print(AttributeError.__doc__)
