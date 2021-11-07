import random
from abc import ABC, abstractmethod


class Figure(ABC):
    __CAPACITY = 10000

    def __init__(self, density):
        self.__density = density

    # Ввод данных из файла.
    @staticmethod
    @abstractmethod
    def file_input(data):
        pass

    # Генерация случайного целочисленного значения.
    @staticmethod
    def _random_int():
        return random.randint(1, Figure.__CAPACITY)

    # Генерация случайного действительного значения.
    @staticmethod
    def _random_float():
        return round(random.uniform(0, Figure._random_int()), random.randint(1, 13))

    # Генерация случайных данных.
    @staticmethod
    @abstractmethod
    def random_input():
        pass

    # Вычисление объема.
    @property
    @abstractmethod
    def volume(self):
        pass

    def __str__(self):
        return "density - {}\n".format(self.__density)
