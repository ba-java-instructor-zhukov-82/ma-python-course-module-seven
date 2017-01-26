##Laboratory Work 7.1.3.

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
        number is a variable value for material quantity should
        be protected
    </li>
    <li>
        place will show place where this material can be placed:
        <ul>
            <li>
                number < 0 = "out of stock"
            </li>
            <li>
                0 < number < 100 = "warehouse"
            </li>
            <li>
                else - "Remote warehouse"
            </li>
        </ul>
    </li>
    <li>
        Create method "plus" for adding material quantity by some count with
        corresponding changing to protected number and place
    </li>
    <li>
        Create method "minus" for decreasing material quantity by some count with
        corresponding changing to number and place
    </li>
    <li>
        Create object for white brick with 300 as initial quantity
    </li>
    <li>
        Create object for brown plank with 20 as initial quantity
    </li>
    <li>
        Print objects variables
    </li>
    <li>
        Add 50 bricks to first object
    </li>
    <li>
        Remove 3 planks from second object
    </li>
</ul>

####Here is the solution code:

*buildings.py*
```python
# Define the class "Building"
class Building:

    # Create class constructor with arguments - material,
    # color, number(with default value - 0) and store place
    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        # number is a variable value
        # for material quantity should
        # be protected
        self._number = number
        self.__store_place = self.__set_store_place()

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number
        self.__store_place = self.__set_store_place()

    material = property(get_material, set_material)
    color = property(get_color, set_color)
    number = property(get_number, set_number)

    # place will show place where this material can
    # be placed:
    #     number < 0 = "out of stock"
    #     number < 100 = "warehouse"
    #     else - "Remote warehouse"
    def __set_store_place(self):
        if self._number < 0:
            return 'Out of stock'
        elif 0 < self._number < 100:
            return 'Warehouse'
        else:
            return 'Remote warehouse'

    def place(self):
        print(self.__store_place)

    # Create method "plus" for adding material
    # quantity by some count with corresponding
    # changing to protected number and place
    def plus(self, number_to_add):
        self._number += number_to_add

    # Create method "minus" for decreasing
    # material quantity by some count with
    # corresponding changing to number and place
    def minus(self, number_to_add):
        self._number -= number_to_add

    def __str__(self):
        return 'Building:\n\tmaterial: {}\n\tcolor: {}\n\tnumber: {}\n'\
               .format(self.__material, self.__color, self._number)

```

*solution_7_2_1.py*
```python
# Create object for white brick with 300 as initial quantity
brick = Building('brick', 'white', 300)

# Create object for brown plank with 20 as initial quantity
plank = Building('plank', 'brown', 20)

# Print objects variables
print(brick)
print(plank)

# Add 50 bricks to first object
brick.plus(50)

# Remove 3 planks from second object
plank.minus(3)


print('50 bricks added to brick-building. Amount: {}'.format(brick.number))
print('3 planks removed from plank-building. Amount: {}'.format(plank.number))
```