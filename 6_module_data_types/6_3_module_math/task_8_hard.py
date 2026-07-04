a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x_1, x_2 = (-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)
    print(min(x_1, x_2), max(x_1, x_2), sep='\n')
elif D == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')
