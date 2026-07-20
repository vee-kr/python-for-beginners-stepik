text, count_plus, count_mult = input(), 0, 0
for char in text:
    if char == '+':
        count_plus += 1
    elif char == '*':
        count_mult += 1

print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_mult, 'раз')
