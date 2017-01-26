from labs.work_7_1_2.solution_7_1_2.buildings import *


brick = Building('brick', 'white', 300)  # create object for white brick with 300 as initial quantity
plank = Building('plank', 'brown', 20)   # create object for brown plank with 20 as initial quantity

# Print objects variables
print(brick)
print(plank)

brick.plus(50)   # add 50 bricks to first object
plank.minus(30)  # remove 3 planks from second object

print('number of bricks:', brick.number)
print('number of planks:', plank.number)