num, flag = int(input()), 'YES'
last = num % 10
while num != 0:
    last_digit = num % 10
    if last_digit < last:
        flag = 'NO'
    last = last_digit
    num //= 10

print(flag)
