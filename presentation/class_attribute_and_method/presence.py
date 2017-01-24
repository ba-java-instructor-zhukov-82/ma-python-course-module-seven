import random


def today_presence(self):
    presence = random.choice(['present', 'absent'])
    print('Student is %s today!' % presence)


def no_attr():
    try:
        raise AttributeError
    except AttributeError:
        print(AttributeError.__doc__)
