m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    population = m * (1 + p / 100) ** i
    print(i + 1, population)
