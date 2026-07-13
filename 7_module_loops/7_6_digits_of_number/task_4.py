num, counter, total, product = int(input()), 0, 0, 1
last = num % 10
while num != 0:
    last_digit = num % 10
    total += last_digit
    counter += 1
    product *= last_digit
    num //= 10

print(total, counter, product, total / counter, last_digit, last_digit + last, sep='\n')
