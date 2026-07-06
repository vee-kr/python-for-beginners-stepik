num_1, num_2 = int(input()), int(input())
for i in range(num_1, num_2 + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)
