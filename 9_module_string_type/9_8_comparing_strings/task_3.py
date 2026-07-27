text_1, text_2 = input().lower(), input().lower()
for char in text_1:
    if not char.isalpha():
        text_1 = text_1.replace(char, '')

for char in text_2:
    if not char.isalpha():
        text_2 = text_2.replace(char, '')

if text_1 == text_2:
    print('YES')
else:
    print('NO')
