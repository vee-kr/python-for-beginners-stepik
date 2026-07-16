s = input()

while len(s) < 10:  # 1. incorrect condition: len(s) <= 10
    if len(s) % 4 == 0:  # 2. incorrect condition: len(s) % 4:
        s = s + 'x'
    elif len(s) % 5 == 0:  # 3. incorrect operation: len(s) // 5 == 0
        s = s + 'y'
    else:
        s = 'z' + s  # 4. incorrect value: s = s + 'z'

s = '@' + s  # 5. incorrect symbol: '&' + s
print(s)
