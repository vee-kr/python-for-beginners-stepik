num_1, num_2, num_3, num_4 = int(input()), int(input()), int(input()), int(input())
if num_1 <= num_2:
    min_1_2 = num_1
else:
    min_1_2 = num_2

if num_3 <= num_4:
    min_3_4 = num_3
else:
    min_3_4 = num_4

if min_1_2 < min_3_4:
    print(min_1_2)
else:
    print(min_3_4)
