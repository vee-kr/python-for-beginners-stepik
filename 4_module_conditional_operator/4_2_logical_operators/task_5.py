num_1, num_2, num_3 = int(input()), int(input()), int(input())
if (num_1 + num_2 > num_3) and (num_1 + num_3 > num_2) and (num_2 + num_3 > num_1):
    print('YES')
else:
    print('NO')
