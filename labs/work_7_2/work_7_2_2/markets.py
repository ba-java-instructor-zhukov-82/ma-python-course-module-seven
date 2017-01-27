# import data from Lab 2
from labs.work_7_2.work_7_2_1.buildings import *


# Define the class "Market" based on class “Building”
class Market(Building):

    # Create class constructor with arguments - material,
    # color, number(with default value - 0), store place
    # and price
    def __init__(self, material, color, number=0, price=0):
        super().__init__(material, color, number)
        self.__price = price

        # Create method "plus" for adding material
        # quantity by some count with corresponding
        # changing to number and place
    def plus(self, quantity):
        self._number += quantity
        self._set_store_place()

    # Create method "minus" for decreasing material
    # quantity by some count with corresponding
    # changing to number and place
    def minus(self, quantity):
        self._number -= quantity
        self._set_store_place()

    def __str__(self):
        return '{}\tprice: {}\n'.format(super().__str__(), str(self.__price))
