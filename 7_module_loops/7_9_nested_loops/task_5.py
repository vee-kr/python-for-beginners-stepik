num = int(input())
for i in range(1, num // 2 + 1):
    print('*' * i)

for k in range(num // 2 + 1, 0, -1):
    print('*' * k)
