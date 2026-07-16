num = int(input())
cnt = 0
total = 1  # 1. incorrect initialization of variable: total = 0
while num % 100 != 11:  # 2. ':' doesn't exist
    if len(str(num)) > 7:  # 3. incorrect condition: len(num) > 7
        cnt += 1

    total += 1  # 4. incorrect extended assignment operator : total = + 1
    num = int(input())

if len(str(num)) > 7: cnt += 1  # 5. lack of condition

print(cnt, '/', total, sep='')
