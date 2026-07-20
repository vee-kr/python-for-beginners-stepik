text, flag = input(), 'Цифр нет'
for char in text:
    if char in '0123456789':
        flag = 'Цифра'

print(flag)
