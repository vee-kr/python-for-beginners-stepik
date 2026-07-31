num, divisors = int(input()), []
for divisor in range(1, num + 1):
    if num % divisor == 0:
        divisors.append(divisor)

print(divisors)
