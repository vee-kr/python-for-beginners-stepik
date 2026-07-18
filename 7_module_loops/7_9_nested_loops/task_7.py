num, count = int(input()), 0
for i in range(1, num + 1):
    for k in range(i):
        count += 1
        print(count, end=' ')
    print()
