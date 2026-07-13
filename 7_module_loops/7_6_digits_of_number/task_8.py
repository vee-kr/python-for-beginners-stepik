num, counter = int(input()), 0
cnt_digits = len(str(num))  # 1
for i in range(1, cnt_digits + 1):
    digit = num // 10 ** (cnt_digits - i) % 10
    if digit % 2 == 0:
        counter += 1
        print(str(counter) + '-я четная цифра равна', digit)
if counter == 0:
    print('Четных цифр в числе нет')

# -----------------------------------------------------

while num != 0:  # 2
    last_digit = num % 10
    if last_digit % 2 == 0:
        counter += 1
        print(str(counter) + '-я четная цифра равна', last_digit)
    num //= 10

if counter == 0:
    print('Четных цифр в числе нет')
