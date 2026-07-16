n = int(input())
while n >= 10:  # 1. incorrect condition: n > 0
    n //= 10  # 2. incorrect operation: n %= 10
print(n)
