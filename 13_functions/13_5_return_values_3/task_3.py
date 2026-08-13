def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    solves = [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
    solves.sort()
    return solves


a, b, c = int(input()), int(input()), int(input())
x_1, x_2 = solve(a, b, c)
print(x_1, x_2)
