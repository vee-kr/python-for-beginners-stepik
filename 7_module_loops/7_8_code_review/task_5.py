n = int(input())
max_digit = -1  # 1. incorrect initialization of variable: max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # 2. incorrect condition: digit < max_digit
            max_digit = digit  # 3. incorrect value of variable: digit = max_digit
    n //= 10  # 4. incorrect operation: n = n % 10
if max_digit == -1:  # 5. incorrect condition: max_digit == 0
    print('NO')
else:
    print(max_digit)
