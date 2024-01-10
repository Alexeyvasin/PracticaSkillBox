from abc import ABC, abstractmethod


class Shape:
    def __init__(self, x, y, length, weight):
        self.__x = x
        self.__y = y
        self.length = length
        self.weight = weight

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_length(self):
        return self.length

    def get_weight(self):
        return self.weight

    def move(self, x, y):
        self.__x = x
        self.__y = y


class ResizableMixin:
    def resize(self, length, weight):
        self.length = length
        self.weight = weight


class Rectangle(Shape, ResizableMixin):
    pass


class Square(Shape, ResizableMixin):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
    pass

rect1 = Rectangle(1,2,3,4)
rect2 = Rectangle(2, 3, 4, 5)
squere1 = Square(1, 2, 3)
for shape in [rect1, rect2, squere1]:
    shape.resize(shape.get_length()*2, shape.get_weight()*2)
    print(shape.get_length(), shape.get_weight())
