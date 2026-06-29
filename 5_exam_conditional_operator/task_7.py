x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
x_12, y_12 = x_1 - x_2, y_1 - y_2
if (-1 <= x_12 <= 1 and (y_12 == 2 or y_12 == -2)) or (-1 <= y_12 <= 1 and (x_12 == 2 or x_12 == -2)):
    print('YES')
else:
    print('NO')
