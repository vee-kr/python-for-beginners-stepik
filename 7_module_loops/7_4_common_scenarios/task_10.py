n, largest_1, largest_2 = int(input()), 0, 0
for _ in range(n):
    num = int(input())
    if num > largest_1:
        largest_1, largest_2 = num, largest_1
    elif num > largest_2:
        largest_2 = num
print(largest_1, largest_2, sep='\n')
