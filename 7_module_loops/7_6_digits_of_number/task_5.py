num = int(input())
while num >= 10:
    last_digit = num % 10
    num //= 10

print(last_digit)
