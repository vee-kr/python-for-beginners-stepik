num = int(input())
first_dig, second_dig = num // 1000, (num % 1000) // 100
third_dig, last_dig = (num % 100) // 10, num % 10

if first_dig + last_dig == second_dig - third_dig:
    print('YES')
else:
    print('NO')
