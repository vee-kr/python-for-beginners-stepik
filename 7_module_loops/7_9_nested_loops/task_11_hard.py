num_1, num_2, total_max, largest = int(input()), int(input()), 0, 0
for i in range(num_1, num_2 + 1):
    total = 0
    for k in range(1, i + 1):
        if i % k == 0:
            total += k
    if total >= total_max:
        total_max = total
        largest = i
        
print(largest, total_max)
