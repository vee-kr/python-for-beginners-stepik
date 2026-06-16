num = int(input())
last_dig = num % 10
middle_dig = num % 100 // 10
first_dig = num // 100
print(num)
print(first_dig, last_dig, middle_dig, sep='')
print(middle_dig, first_dig, last_dig, sep='')
print(middle_dig, last_dig, first_dig, sep='')
print(last_dig, first_dig, middle_dig, sep='')
print(last_dig, middle_dig, first_dig, sep='')

