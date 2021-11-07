from math import sqrt
from figure import Figure


class Tetrahedron(Figure):
    def __init__(self, density, edge):
        super().__init__(density)
        self.__edge = edge

    # Ввод данных из файла.
    @staticmethod
    def file_input(data):
        density = float(next(data))
        edge = int(next(data))
        return Tetrahedron(density, edge)

    # Генерация случайных данных.
    @staticmethod
    def random_input():
        density = Tetrahedron._random_float()
        edge = Tetrahedron._random_int()
        return Tetrahedron(density, edge)

    # Вычисление объема.
    @property
    def volume(self):
        return sqrt(2) / 12 * self.__edge ** 3

    def __str__(self):
        return "Tetrahedron, edge - {}, {}".format(self.__edge, super().__str__())
