num, old_numbers, value_func, numbers = int(input()), [], list(), []

for _ in range(num):  # 1
    cur_num = int(input())
    old_numbers.append(cur_num)
    value_func.append(cur_num ** 2 + 2 * cur_num + 1)

print(*old_numbers, sep='\n')
print()
print(*value_func, sep='\n')

# --------------------------------

for _ in range(num):  # 2
    cur_num = int(input())
    numbers.append(cur_num)
    numbers.append(cur_num ** 2 + 2 * cur_num + 1)

print(*numbers[::2], sep='\n')
print()
print(*numbers[1::2], sep='\n')
