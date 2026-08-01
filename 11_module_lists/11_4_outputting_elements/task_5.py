num, numbers = int(input()), []
for _ in range(num):
    numbers.append(int(input()))

for i in range(len(numbers)):  # 1
    if numbers[i] == max(numbers):
        largest_index = i
    if numbers[i] == min(numbers):
        smallest_index = i

del numbers[max(largest_index, smallest_index)]
del numbers[min(smallest_index, largest_index)]

print(*numbers, sep='\n')

# ---------------

for dig in numbers:  # 2
    if dig != max(numbers) and dig != min(numbers):
        print(dig)
