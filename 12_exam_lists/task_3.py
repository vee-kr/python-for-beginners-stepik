numbers = [int(i) for i in input().split()]
print(*numbers, sep='+', end='=')
print(sum(numbers))
