n = int(input())  # 1. incorrect initialization of variable: n = input()
product = 1  # 2. incorrect initialization of variable: product = n % 10
while n > 0:  # 3. incorrect condition: n >= 10
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
