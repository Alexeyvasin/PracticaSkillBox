from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color=0, velocity=0):
        self.__color = color
        self.__velocity = velocity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @abstractmethod
    def move(self):
        print('Двигаюсь')

    def klaxon(self):
        print('Сигналю')


class MusicMixin:
    def play_music(self):
        print('Играю музыку')


class Auto(Transport):

    def move(self):
        print('Еду по земле')


class Boat(Transport):

    def move(self):
        print('Иду по воде')


class Amphibian(Transport, MusicMixin):

    def move(self):
        print('Еду и по воде и по земле')


amp = Amphibian('red', 20)
amp.move()
amp.play_music()
print(amp.velocity)
print(amp.color)
