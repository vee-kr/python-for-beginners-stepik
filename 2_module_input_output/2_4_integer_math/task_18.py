num = int(input())
last_dig = num % 10
third_dig = num % 100 // 10
second_dig = num % 1000 // 100
first_dig = num // 1000
print('Цифра в позиции тысяч равна', first_dig)
print('Цифра в позиции сотен равна', second_dig)
print('Цифра в позиции десятков равна', third_dig)
print('Цифра в позиции единиц равна', last_dig)


