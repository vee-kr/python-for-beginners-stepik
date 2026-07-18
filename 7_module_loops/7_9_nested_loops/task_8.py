num_1, num_2 = int(input()), int(input())
for i in range(num_1, num_2 + 1):
    count = 0
    for k in range(1, i + 1):
        if i % k == 0:
            count += 1
    if count == 2 and i != 1:
        print(i)
