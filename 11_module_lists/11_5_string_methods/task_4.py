sequence = input().split()
for i in range(len(sequence)):
    for k in range(int(sequence[i])):
        print('+', end='')
    print()
