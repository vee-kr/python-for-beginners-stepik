num, total = int(input()), 0
for i in range(1, num + 1):
    total += (-1) ** (i + 1) * i
print(total)
