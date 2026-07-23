num, count = int(input()), 0
for i in range(1, num + 1):
    text = input()
    if text.count('11') >= 3:
        count += 1
print(count)
