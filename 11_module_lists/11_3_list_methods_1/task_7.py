num, numbers = int(input()), []
for _ in range(num):
    numbers.append(int(input()))

del numbers[1::2]
print(numbers)
