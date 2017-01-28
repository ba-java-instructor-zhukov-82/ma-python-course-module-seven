from examples.factory.cars.abstract import AbstractCar


class Taxi(AbstractCar):

    TYPE = 'TAXI'

    def __str__(self):
        return '{} {}'.format(super().__str__(), 'taxi')
