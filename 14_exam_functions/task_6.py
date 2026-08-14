def is_magic(date):
    numbers = [int(i) for i in date.split('.')]
    return numbers[0] * numbers[1] == numbers[2] % 100


date = input()
print(is_magic(date))
