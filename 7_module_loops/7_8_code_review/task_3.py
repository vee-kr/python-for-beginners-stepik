s = 0  # 1. incorrect initialization of variable: s = 1
for _ in range(1, 8):  # 2. incorrect boundary: range(1, 7)
    n = int(input())  # 3. incorrect initialization of variable: n = input()
    if n % 2 == 0:  # 4. incorrect condition: i % 2 == 0
        s = s + n
print(s)
