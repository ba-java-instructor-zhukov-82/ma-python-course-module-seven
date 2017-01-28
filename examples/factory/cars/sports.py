from examples.factory.cars.abstract import AbstractCar


class SportCar(AbstractCar):

    TYPE = 'SPORT_CAR'

    def __str__(self):
        return '{} {}'.format(super().__str__(), 'sport')
