n = 8  # 1. incorrect initialization of variable: n = 7
count = 0
maximum = - 10 ** 12  # 2. incorrect initialization of variable: maximum = 1000
for _ in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:  # 3. incorrect operation: x // 4 == 0
        count += 1
        if x > maximum:  # 4. incorrect condition: x < maximum
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
