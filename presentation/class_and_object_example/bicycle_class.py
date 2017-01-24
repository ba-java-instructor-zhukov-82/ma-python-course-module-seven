class Bicycle:
    cadence = 0
    speed = 0
    gear = 1

    def changeCadence(self, newValue):
        self.cadence = newValue

    def changeGear(self, newValue):
        self.gear = newValue

    def speedUp(self, increment):
        self.speed = self.speed + increment

    def applyBrakes(self, decrement):
        self.speed = self.speed - decrement

    def printStates(self):
        print("cadence:%s,speed:%s,gear:%s." % (self.cadence, self.speed, self.gear))
