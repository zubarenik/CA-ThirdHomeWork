from figure import Figure


class Parallelepiped(Figure):
    def __init__(self, density, first_edge, second_edge, third_edge):
        super().__init__(density)
        self.__first_edge = first_edge
        self.__second_edge = second_edge
        self.__third_edge = third_edge

    # Ввод данных из файла.
    @staticmethod
    def file_input(data):
        density = float(next(data))
        first_edge = int(next(data))
        second_edge = int(next(data))
        third_edge = int(next(data))
        return Parallelepiped(density, first_edge, second_edge, third_edge)

    # Генерация случайных данных.
    @staticmethod
    def random_input():
        density = Parallelepiped._random_float()
        first_edge = Parallelepiped._random_int()
        second_edge = Parallelepiped._random_int()
        third_edge = Parallelepiped._random_int()
        return Parallelepiped(density, first_edge, second_edge, third_edge)

    # Вычисление объема.
    @property
    def volume(self):
        return self.__first_edge * self.__second_edge * self.__third_edge

    def __str__(self):
        return "Parallelepiped, first edge - {}, second edge - {}, third edge - {}, {}".format(self.__first_edge,
                                                                                               self.__second_edge,
                                                                                               self.__third_edge,
                                                                                               super().__str__())
