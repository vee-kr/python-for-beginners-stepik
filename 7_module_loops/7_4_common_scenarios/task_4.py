num, total = int(input()), 0
for i in range(1, num + 1):
    if i ** 2 % 10 == 5:
        total += i
print(total)
