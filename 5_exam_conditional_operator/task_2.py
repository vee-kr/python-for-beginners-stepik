x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
if ((x_1 % 2 == 0 and y_1 % 2 != 0) or (x_1 % 2 != 0 and y_1 % 2 == 0)) and (
        (x_2 % 2 == 0 and y_2 % 2 != 0) or (x_2 % 2 != 0 and y_2 % 2 == 0)):
    print('YES')  # for black squares
elif ((x_1 % 2 != 0 and y_1 % 2 != 0) or (x_1 % 2 == 0 and y_1 % 2 == 0)) and (
        (x_2 % 2 != 0 and y_2 % 2 != 0) or (x_2 % 2 == 0 and y_2 % 2 == 0)):
    print('YES')  # for white squares
else:
    print('NO')
