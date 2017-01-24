class Building:  # Define class 'Building'

    # - Create class constructor with arguments - material,
    # - Material that will accept name for building material
    # - Color that will accept color for building material
    # - Number is a variable value for material quantity
    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        self.__number = number

    # Place will show place where this material can be placed:
    #     - number < 0 = "out of stock"
    #     - 0 < number < 100 = "warehouse"
    #     - else - "Remote warehouse
    def place(self):
        if self.__number < 0:
            print('Out of stock')
        elif 0 < self.__number < 100:
            print('Warehouse')
        else:
            print('Remote warehouse')

obj1 = Building('wood', 'brown', -20)  # create first object of the class "Building
obj2 = Building('stone', 'grey', 10)   # create second object of the class "Building
obj3 = Building('stone', 'grey', 110)  # create third object of the class "Building

obj1.place()  # 'Out of stock'
obj2.place()  # 'Warehouse'
obj3.place()  # 'Remote warehouse'