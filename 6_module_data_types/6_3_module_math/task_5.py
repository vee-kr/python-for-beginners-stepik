from math import pi, tan

count, side = int(input()), float(input())
S = (count * side ** 2) / (4 * tan(pi / count))
print(S)
