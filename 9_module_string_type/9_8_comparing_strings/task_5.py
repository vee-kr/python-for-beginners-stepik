num = int(input())
alphabet = 'АБВГДЕЖЗИЙКЛМНОП'
for _ in range(num):
    class_name = input()
    if len(class_name) == 2 and (class_name[0].isdigit()) and class_name[-1] in alphabet:
        print('YES')
    else:
        print('NO')
