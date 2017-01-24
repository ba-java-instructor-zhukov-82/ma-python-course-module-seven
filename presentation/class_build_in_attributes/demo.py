from presentation.class_attribute_and_method.students import Student

print('Student.__doc__:', Student.__doc__)
print('Student.__name__:', Student.__name__)
print('Student.__module__:', Student.__module__)
print('Student.__bases__:', Student.__bases__)

print('Student.__dict__:')
for element in Student.__dict__:
    print('\t', element)

