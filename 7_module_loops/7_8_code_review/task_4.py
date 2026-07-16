count = 0
p = 1  # 1. incorrect initialization of variable: p = 0
for i in range(1, 11):  # 2. incorrect boundary: range(1, 10)
    x = int(input())
    if x >= 0:  # 3. incorrect condition: x > 0
        p = p * x
        count = count + 1
if count > 0:
    print(count)  # 4. incorrect output: print(x)
    print(p)
else:
    print('NO')
