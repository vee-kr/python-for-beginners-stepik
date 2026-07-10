num_1, num_2, num = 1, 0, int(input())
for _ in range(num):
    num_1, num_2 = num_2, num_1 + num_2
    print(num_2, end=' ')
