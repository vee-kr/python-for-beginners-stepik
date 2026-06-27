num_1, num_2, num_3 = int(input()), int(input()), int(input())
if (num_1 < num_2 < num_3) or (num_3 < num_2 < num_1):
    print(num_2)
elif (num_2 < num_1 < num_3) or (num_3 < num_1 < num_2):
    print(num_1)
else:
    print(num_3)
