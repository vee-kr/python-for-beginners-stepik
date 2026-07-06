num_1, num_2 = int(input()), int(input())
for i in range(num_1, num_2 - 1, -1):  # 1
    if i % 2 != 0:
        print(i)

if num_1 % 2 == 0:  # 2
    num_1 = num_1 - 1
for i in range(num_1, num_2 - 1, -2):
    print(i)
