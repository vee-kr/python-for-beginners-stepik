num = int(input())
while num >= 10:
    total = 0
    while num != 0:
        last = num % 10
        total += last
        num //= 10
    num = total

print(num)
