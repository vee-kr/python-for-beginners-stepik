num_1, num_2, count = int(input()), int(input()), 0
for i in range(1, num_1):
    for k in range(1, num_1):
        for j in range(1, num_1):
            if i + 3 * k + 2 * j == num_2:
                print(i, ' + 3×', k, ' + 2×', j, ' = ', num_2, sep='')
                count += 1
if count == 0:
    print('При заданных n и m решений не существует.')
