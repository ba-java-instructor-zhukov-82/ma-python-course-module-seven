from labs.work_7_2.work_7_2_1.buildings import *


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