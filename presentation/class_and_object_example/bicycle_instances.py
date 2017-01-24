from presentation.class_and_object_example.bicycle_class import Bicycle

# Create two different Bicycle objects
bike1 = Bicycle()
bike2 = Bicycle()

# Invoke methods on those objects
bike1.changeCadence(50)
bike1.speedUp(10)
bike1.changeGear(2)
bike1.printStates()

bike2.changeCadence(50)
bike2.speedUp(10)
bike2.changeGear(2)
bike2.changeCadence(40)
bike2.speedUp(10)
bike2.changeGear(3)
bike2.printStates()
