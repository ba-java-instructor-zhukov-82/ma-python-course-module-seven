##Laboratory Work 7.2.2.

<p>
    <span>
          Write an object oriented program that show
          building material property and storage quantity:
    </span>
</p>

<ul>
    <li>
        import data from Lab 2
    </li>
    <li>
        Define the class "Market" based on class “Building”
    </li>
    <li>
        Create class constructor with arguments - material,
        color, number (with default value - 0), store place
        and price
    </li>
    <li>
        All attributes should be get from class Building except price
    </li>
    <li>
        Create method "plus" for adding material quantity by some count
        with corresponding changing to number and place
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

*markets.py*
```python
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
```

*solution_7_2_2.py*
```python
# Create object for white brick with 300 as initial quantity
brick_market = Market('brick', 'white', 300, price=12)

# Create object for brown plank with 20 as initial quantity
plank_market = Market('plank', 'brown', 20, price=20)

# Print objects variables
print(brick_market)
print(plank_market)

# Add 50 bricks to first object
brick_market.plus(50)

# Remove 3 planks from second object
plank_market.minus(3)


print('50 bricks added to brick-building. Amount: {}'.format(brick_market.number))
print('3 planks removed from plank-building. Amount: {}'.format(plank_market.number))
```