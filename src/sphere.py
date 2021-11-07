from math import pi
from figure import Figure


class Sphere(Figure):
    def __init__(self, density, radius):
        super().__init__(density)
        self.__radius = radius

    # Ввод данных из файла.
    @staticmethod
    def file_input(data):
        density = float(next(data))
        radius = int(next(data))
        return Sphere(density, radius)

    # Генерация случайных данных.
    @staticmethod
    def random_input():
        density = Sphere._random_float()
        radius = Sphere._random_int()
        return Sphere(density, radius)

    # Вычисление объема.
    @property
    def volume(self):
        return pi * self.__radius ** 3 * 4 / 3

    def __str__(self):
        return "Sphere, radius - {}, {}".format(self.__radius, super().__str__())
