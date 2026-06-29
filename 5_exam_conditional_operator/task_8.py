x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
if x_1 == x_2 or y_1 == y_2 or ((x_2 - x_1 == y_2 - y_1) or (y_2 - y_1 == x_1 - x_2)):
    print('YES')
else:
    print('NO')
