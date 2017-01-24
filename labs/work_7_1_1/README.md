##Laboratory Work 7.1.1.

<p>
    <span>
          Write an object oriented program that show
          building material property and storage quantity:
    </span>
</p>

<ul>
    <li>
        Define the class "Building"
    </li>
    <li>
        Create class constructor with arguments - material,
        color, number (with default value - 0) and store place
    </li>
    <li>
        Material that will accept name for building material
    </li>
    <li>
        Color that will accept color for building material
    </li>
    <li>
        Number is a variable value for material quantity
    </li>
    <li>
        Place will show place where this material can be placed:
        <ul>
            <li>
                number < 0 = "out of stock"
            </li>
            <li>
                0 < number < 100 = "warehouse"
            </li>
            <li>
                else - "Remote warehouse
            </li>
        </ul>
    </li>
</ul>

####Here is the solution code:

*solution_7_1_1.py*
```python
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

obj1 = Building('wood', 'brown', -20)   # create first object of the class "Building
obj2 = Building('stone', 'grey', 10)   # create second object of the class "Building
obj3 = Building('stone', 'grey', 110)   # create second object of the class "Building

obj1.place()
obj2.place()
obj3.place()
```