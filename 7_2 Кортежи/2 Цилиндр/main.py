import math


def s_cylinder(rad, h):
    side = 2 * math.pi * h
    s_full = side + ((2 * math.pi) * (rad ** 2))
    return side, s_full


radius = float(input('Введите радиус цилиндра: '))
height = float(input('Введите высоту цилиндра: '))
s_side, full = s_cylinder(radius, height)
print('\nПлощадь боковой поверхности: {:.2f}\nПолная площадь: {:.2f}'.format(s_side, full))
