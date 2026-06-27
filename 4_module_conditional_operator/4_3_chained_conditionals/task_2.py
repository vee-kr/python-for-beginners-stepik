side_1, side_2, side_3 = int(input()), int(input()), int(input())
if side_1 == side_2 == side_3:
    print('Равносторонний')
elif side_1 != side_2 != side_3 and side_1 != side_3:
    print('Разносторонний')
else:
    print('Равнобедренный')
