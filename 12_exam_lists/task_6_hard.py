phone_numbers = [i for i in input().split('-') if i.isdigit()]

if 3 <= len(phone_numbers) <= 4:  # 1
    if phone_numbers[0] == '7' and len(phone_numbers[1]) == len(phone_numbers[2]) == 3 and len(
            phone_numbers[3]) == 4:
        print('YES')
    elif len(phone_numbers[0]) == len(phone_numbers[1]) == 3 and len(phone_numbers[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# -------

lengths = [len(i) for i in phone_numbers]  # 2
if 3 <= len(lengths) <= 4:
    if lengths == [3, 3, 4] or (lengths == [1, 3, 3, 4] and phone_numbers[0] == '7'):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
