from examples.factory.cars.factory import CarFactory
from examples.factory.cars.sports import SportCar
from examples.factory.cars.taxis import Taxi

sport_car = CarFactory.get_instance(SportCar.TYPE)
taxi = CarFactory.get_instance(Taxi.TYPE)

for car in [sport_car, taxi]:
    print(car)
