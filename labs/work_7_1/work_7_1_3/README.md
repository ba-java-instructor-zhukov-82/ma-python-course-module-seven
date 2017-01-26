##Laboratory Work 7.1.3.

<p>
    <span>
          Write an object oriented program that show building
          material property and storage quantity:
    </span>
</p>

<ul>
    <li>
        import all data from Lab 2
    </li>
    <li>
        Create object for yellow brick with 200 as initial quantity
    </li>
    <li>
        Create object for red plank with 10 as initial quantity
    </li>
    <li>
        Print objects variables
    </li>
    <li>
        Add 1 bricks to first object
    </li>
    <li>
        Remove 2 planks from second object
    </li>
</ul>

####Here is the solution code:

*solution_7_1_3.py*
```python
# import all data from Lab 2
from labs.work_7_1.work_7_1_2.solution_7_1_2.buildings import *

# Create object for yellow brick with 200 as initial quantity
brick = Building('brick', 'yellow', 200)
# Create object for red plank with 10 as initial quantity
plank = Building('plank', 'red', 10)

# Print objects variables
print(brick)
print(plank)

# Add 1 bricks to first object
brick.plus(1)
# Remove 2 planks from second object
plank.minus(2)

print('One brick added to brick-building. Left: {}'.format(brick.get_number()))
print('Two planks removed from plank-building. Left: {}'.format(plank.get_number()))

```