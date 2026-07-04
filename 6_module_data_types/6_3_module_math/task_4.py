from math import radians, sin, cos, tan

x = float(input())
r = radians(x)
print(sin(r) + cos(r) + tan(r) ** 2)
