#  builtins
import builtins


def cur_package_path():
    return str(__file__)[:str(__file__).rfind('/') + 1]


def open_file(path):
    f = builtins.open(path, 'r')
    return Capitalizator(f)


class Capitalizator:

    # Class Capitalizator - wrapper around a file that converts output to upper-case.

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        capitalized_content = self._f.read(count).upper()
        self._f.close()
        return capitalized_content


file_name = 'text.txt'
file_path = cur_package_path() + 'files/' + file_name

file = open(file_path, 'r')
print('\n\tOpened with common file object:', file.read())
file.close()

capitalizator = open_file(file_path)
print('\n\tOpened with Capitalizator instance:', capitalizator.read())
