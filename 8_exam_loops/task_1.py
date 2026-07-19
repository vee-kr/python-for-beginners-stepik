n = int(input())  # 1. incorrect initialization of variable: n = input()
s = 0
while n > 0:  # 2. incorrect condition: n > 10
    if n % 2 == 0:  # 3. incorrect condition: n % 2 == 1
        s += n % 10  # 4. incorrect operation: s = n % 10
    n //= 10
print(s)
