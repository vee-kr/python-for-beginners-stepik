num_1, num_2, sign = int(input()), int(input()), input()
if sign == '+':
    print(num_1 + num_2)
elif sign == '-':
    print(num_1 - num_2)
elif sign == '*':
    print(num_1 * num_2)
elif sign == '/':
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
