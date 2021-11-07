import random
from sphere import Sphere
from parallelepiped import Parallelepiped
from tetrahedron import Tetrahedron


class Container:
    __CAPACITY = 10000

    def __init__(self):
        self.__figures = []

    @property
    def size(self):
        return len(self.__figures)

    # Ввод данных из файла.
    def file_input(self, data):
        try:
            while True:
                type = int(next(data))
                if self.size == self.__CAPACITY:
                    raise ValueError("Can`t be more than {} objects!".format(self.__CAPACITY))

                if type == 1:
                    figure = getattr(Sphere, 'file_input')
                elif type == 2:
                    figure = getattr(Parallelepiped, 'file_input')
                elif type == 3:
                    figure = getattr(Tetrahedron, 'file_input')
                else:
                    raise ValueError("An object of this type does not exist!")
                self.__figures.append(figure(data))
        except StopIteration:
            return
        except ValueError as exception:
            print(exception)
            print("Only first {} objects are loaded!".format(self.size))

    # Случайная генерация данных.
    def random_input(self, size):
        if size < 0:
            raise ValueError("Size must be more than zero!")

        while self.size < size:
            if self.size == self.__CAPACITY:
                print("Can`t be more than {} objects!".format(self.__CAPACITY))
                break

            type = random.randint(1, 3)
            if type == 1:
                figure = getattr(Sphere, 'random_input')
            elif type == 2:
                figure = getattr(Parallelepiped, 'random_input')
            else:
                figure = getattr(Tetrahedron, 'random_input')
            self.__figures.append(figure())

    # Вывод результата в файл.
    def file_output(self, file):
        file.write("\nContainer's size - {}\n".format(self.size))

        for index, figure in enumerate(self.__figures):
            file.write("{}: {}".format(index + 1, figure))

    # Меняет элементы местами.
    def swap(self, i):
        self.__figures[i], self.__figures[i - 1] = self.__figures[i - 1], self.__figures[i]

    # Сортировка Shaker Sort.
    def shaker_sort(self):
        left, right = 1, self.size - 1

        while left <= right:
            for i in range(right, left - 1, -1):
                if self.__figures[i - 1].volume < self.__figures[i].volume:
                    self.swap(i)
            left += 1
            for i in range(left, right + 1):
                if self.__figures[i - 1].volume < self.__figures[i].volume:
                    self.swap(i)
            right -= 1
