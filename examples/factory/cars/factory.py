from examples.factory.cars.sports import SportCar
from examples.factory.cars.taxis import Taxi


class CarFactory:

    @staticmethod
    def get_instance(car_type=SportCar.TYPE):
        if car_type == SportCar.TYPE:
            return SportCar()
        elif car_type == Taxi.TYPE:
            return Taxi()
        else:
            print('Incorrect car type passed!')
            return None
