num, counter_3, counter_last, counter_even, total_greater_5, product_greater_7, counter_0_5 = int(
    input()), 0, 0, 0, 0, 1, 0
last = num % 10
while num != 0:
    current_digit = num % 10
    if current_digit == 3:
        counter_3 += 1
    if current_digit == last:
        counter_last += 1
    if current_digit % 2 == 0:
        counter_even += 1
    if current_digit > 5:
        total_greater_5 += current_digit
    if current_digit > 7:
        product_greater_7 *= current_digit
    if current_digit == 5 or current_digit == 0:
        counter_0_5 += 1
    num //= 10
print(counter_3, counter_last, counter_even, total_greater_5, product_greater_7, counter_0_5, sep='\n')
