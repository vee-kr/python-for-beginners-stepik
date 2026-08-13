from math import pi


def get_circle(radius):
    length = 2 * pi * radius
    area = pi * radius ** 2
    return length, area


R = float(input())

length_circle, area_circle = get_circle(R)
print(length_circle, area_circle)
