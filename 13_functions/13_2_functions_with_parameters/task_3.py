def print_digit_sum(num):
    total = 0
    for i in str(num):
        total += int(i)
    print(total)


num = int(input())
print_digit_sum(num)
