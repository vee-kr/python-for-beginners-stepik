num, smallest, biggest = int(input()), 9, 0
while num > 0:
    last_digit = num % 10
    biggest = max(biggest, last_digit)
    smallest = min(smallest, last_digit)
    num //= 10

print('Максимальная цифра равна', biggest)
print('Минимальная цифра равна', smallest)
