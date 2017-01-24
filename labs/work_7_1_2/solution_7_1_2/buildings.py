class Building:

    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        self.__number = number

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    material = property(get_material, set_material)
    color = property(get_color, set_color)
    number = property(get_number, set_number)

    def place(self):
        if self.__number < 0:
            print('Out of stock')
        elif 0 < self.__number < 100:
            print('Warehouse')
        else:
            print('Remote warehouse')

    # Create method "plus" for adding material quantity by some
    # count with corresponding changing to number and place
    def plus(self, number_to_add):
        self.__number += number_to_add

    # Create method minus" for decreasing material quantity by some
    # count with corresponding changing to number and place
    def minus(self, number_to_add):
        self.__number -= number_to_add

    def __str__(self):
        return 'Building:\n\tmaterial: {}\n\tcolor: {}\n\tnumber: {}\n'\
               .format(self.__material, self.__color, self.__number)


brick = Building('brick', 'white', 300)  # create object for white brick with 300 as initial quantity
plank = Building('plank', 'brown', 20)   # create object for brown plank with 20 as initial quantity

# Print objects variables
print(brick)
print(plank)

brick.plus(50)   # add 50 bricks to first object
plank.minus(30)  # remove 3 planks from second object

print('number of bricks:', brick.number)
print('number of planks:', plank.number)
