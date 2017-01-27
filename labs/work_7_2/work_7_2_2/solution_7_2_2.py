from labs.work_7_2.work_7_2_2.markets import Market

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