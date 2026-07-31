num, strings = int(input()), []
for _ in range(num):
    strings.append(input())

index = int(input())
for i in range(len(strings)):
    if len(strings[i]) >= index:
        print(strings[i][index - 1], end='')
    else:
        continue
