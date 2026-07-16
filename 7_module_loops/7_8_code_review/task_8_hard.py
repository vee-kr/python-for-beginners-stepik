mx = -10 ** 6  # 1. incorrest initialization of variable: mx = 0
s = 0
for _ in range(10):  # 2. incorrect boundary: range(11)
    x = int(input())
    if x < 0:
        s += x  # 3. incorrect extended assignment operator: s = x
        if x > mx:  # 4. incorrect indentation
            mx = x
if s == 0:  # 5. lack of condition
    print('NO')
else:
    print(s)
    print(mx)
