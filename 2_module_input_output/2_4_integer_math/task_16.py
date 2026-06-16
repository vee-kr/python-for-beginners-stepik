num = int(input())
last_dig = num % 10
middle_dig = num % 100 // 10
first_dig = num // 100
total = last_dig + middle_dig + first_dig
product = last_dig * middle_dig * first_dig
print('The total of digits equals', total)
print('The product of digits equals123', product)