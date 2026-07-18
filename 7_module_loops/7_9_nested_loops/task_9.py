num, total = int(input()), 0
for i in range(1, num + 1):
    product = 1
    for k in range(1, i + 1):
        product *= k
    total += product

print(total)
