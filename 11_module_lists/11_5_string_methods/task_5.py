ip, flag = input().split('.'), 'ДА'
for num in ip:
    if not (0 <= int(num) <= 255):
        flag = 'НЕТ'
        break
print(flag)
